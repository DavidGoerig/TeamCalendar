from .models import SequenceDefinition, Levels, Sequences
from .forms import ParametersLevelForm, LevelDefinitionForm, SetupForm, SequenceDefinitionForm, DeviceNamesForm, SequencesForm

def delete_level(param_id, level_id, levels):
    to_delete = levels.get(id=param_id).lvl_def.get(id=level_id)
    lvl_nbr_del = to_delete.lvl_nbr
    to_delete.delete()
    levels_to_manage = levels.get(id=param_id).lvl_def.all()
    for lvl in levels_to_manage:
        if lvl.lvl_nbr > lvl_nbr_del:
            lvl.lvl_nbr = lvl.lvl_nbr - 1
            lvl.save()

def delete_sequence(id, sequence, id_sequence):
    sequence_to_modify = sequence.get(id=id_sequence)
    to_delete = sequence_to_modify.seq.get(id=id)
    seq_nbr_del = to_delete.order_number
    to_delete.delete()
    for seq in sequence_to_modify.seq.all():
        if seq.order_number > seq_nbr_del:
            seq.order_number = seq.order_number - 1
            seq.save()

def add_level(lvlform, levels, id):
    new_level = lvlform.save()
    if levels.get(id=id).lvl_def.all().count() is 0:
        new_level.lvl_nbr = 1
        new_level.save()
    else:
        higher_lvl = levels.get(id=id).lvl_def.order_by('lvl_nbr').reverse()[0].lvl_nbr
        if new_level.lvl_nbr > higher_lvl or new_level.lvl_nbr < 1:
            new_level.lvl_nbr = higher_lvl + 1
            new_level.save()
        elif new_level.lvl_nbr <= higher_lvl and new_level.lvl_nbr >= 1:
            levels.get(id=id).lvl_def.get(lvl_nbr=new_level.lvl_nbr).delete()
    levels.get(id=id).lvl_def.add(new_level)

def choose_level(levels, sequence, id_param, id_level, id_sequence):
    prm = levels.get(id=id_param).param
    lvl = levels.get(id=id_param).lvl_def.get(id=id_level).lvl_nbr
    order_nbr = 1
    sequence_to_modify = sequence.get(id=id_sequence)
    if sequence_to_modify.seq.all().count() is not 0:
        order_nbr = sequence_to_modify.seq.order_by('order_number').reverse()[0].order_number + 1
    new_seq = SequenceDefinition(order_number=order_nbr, param=prm, level=lvl, pause_time=0)
    new_seq.save()
    sequence_to_modify.seq.add(new_seq)

def parameter_validation(form, levels, project):
    new_param = form.save()
    if levels.filter(param=new_param).count() is 0:
        new_level = Levels(param=new_param)
        new_level.save()
        levels.add(new_level)
        project.save()

def setup_validation(proj_form, project):
    cd = proj_form.cleaned_data
    type = cd.get('project_type')
    sample_prep = cd.get('sample_prep_method')
    project.setup.project_type = type
    project.setup.sample_prep_method = sample_prep
    project.setup.save()
    project.save()

def pause_validation(pause_form, sequence, id_sequence):
    sequence_to_modify = sequence.get(id=id_sequence)
    cd = pause_form.cleaned_data
    pause_time = cd.get('pause_time')
    pause_def = cd.get('break_def')
    order_nbr = 1
    if sequence_to_modify.seq.all().count() is not 0:
        order_nbr = sequence_to_modify.seq.order_by('order_number').reverse()[0].order_number + 1
    if pause_time <= 0:
        pause_time = 1
    new_seq = SequenceDefinition(order_number=order_nbr, param="None", level=0, pause_time=pause_time, break_def=pause_def)
    new_seq.save()
    sequence_to_modify.seq.add(new_seq)

def device_validation(device_form, project):
    new_device = device_form.save()
    project.setup.devices_names.add(new_device)
    project.setup.save()
    project.save()

def settings_main(project, request):
    levels = project.setup.levels
    levels_disp = project.setup.levels.all()
    device_disp = project.setup.devices_names.all()

    sequence = project.setup.seq_def
    sequence_disp = project.setup.seq_def.all()
    lastid = None

    lvlform = LevelDefinitionForm(None)
    pause_form = SequenceDefinitionForm(None)
    if request.method == 'POST' and ("addpause" in request.POST):
        pause_form = SequenceDefinitionForm(request.POST or None)
    if pause_form.is_valid():
        pause_validation(pause_form, sequence_disp, sequence)

    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "deleteparam":
            levels.get(id=id[1]).delete()
        elif id[0] == "deletelvl":
            delete_level(id[1], id[2], levels)
            lastid = int(id[1])
        elif id[0] == "addlevel":
            lvlform = LevelDefinitionForm(request.POST or None)
            if lvlform.is_valid():
                add_level(lvlform, levels, id[1])
                lastid = int(id[1])
            lvlform = LevelDefinitionForm(None)
        elif id[0] == "chooselvl":
            choose_level(levels, sequence, id[1], id[2], id[3])
            lastid = int(id[3])
        elif id[0] == "deletesequence":
            sequence.get(id=id[1]).delete()
        elif id[0] == "deletesequencelevel":
            delete_sequence(id[1], sequence, id[2])
            lastid = int(id[2])
        elif id[0] == "deletedevice":
            project.setup.devices_names.get(id=id[1]).delete()
        elif id[0] == "addpause":
            pause_form = SequenceDefinitionForm(request.POST or None)
            if pause_form.is_valid():
                pause_validation(pause_form, sequence, id[1])
            lastid = int(id[1])

    form = ParametersLevelForm(None)
    if request.method == 'POST' and ("addparam" in request.POST):
        form = ParametersLevelForm(request.POST or None)
    if form.is_valid():
        parameter_validation(form, levels, project)
        form = ParametersLevelForm(None)

    seqform = SequencesForm(None)
    if request.method == 'POST' and ("addsequence" in request.POST):
        seqform = SequencesForm(request.POST or None)
    if seqform.is_valid():
        cd = seqform.cleaned_data
        new_seq_name = cd.get('name')
        sample_type = cd.get('sample_type')
        sample_matrix = cd.get('sample_matrix')
        if new_seq_name is None:
            new_seq_name = "Sequence"
        if sequence.filter(name=new_seq_name).count() is 0:
            new_seq = Sequences(name=new_seq_name, sample_type=sample_type, sample_matrix=sample_matrix)
            new_seq.save()
            sequence.add(new_seq)
            project.save()
            seqform = SequencesForm(None)

    proj_form = SetupForm(instance=project.setup)
    if request.method == 'POST' and ("setprojtype" in request.POST):
        proj_form = SetupForm(request.POST or None)
    if proj_form.is_valid():
        setup_validation(proj_form, project)

    device_form = DeviceNamesForm(None)
    if request.method == 'POST' and ("adddevice" in request.POST):
        device_form = DeviceNamesForm(request.POST or None)
    if device_form.is_valid():
        device_validation(device_form, project)
    return levels, levels_disp, device_disp, sequence, sequence_disp, lastid, lvlform, pause_form, form, seqform, proj_form, device_form