from .models import Project, Setup, Information, DeviceNames, SequenceDefinition, Levels, LevelDefinition, Content, Sequences

def copy_project(id_template, project_name):
    try:
        template_to_copy = Project.objects.get(id=id_template)
    except Project.DoesNotExist:
        template_to_copy = None
    if template_to_copy is None or template_to_copy.is_template is False:
        return -1
    # Copy information
    if template_to_copy.information is not None:
        new_info = Information(project_nbr=template_to_copy.information.project_nbr,
                           area=template_to_copy.information.area,
                           test_plan=template_to_copy.information.test_plan,
                           responsable_name=template_to_copy.information.responsable_name,
                           eln_number=template_to_copy.information.eln_number,
                           test_report=template_to_copy.information.test_report)
    else:
        new_info = Information()
    new_info.save()
    #Copy Setup
    if template_to_copy.setup is not None:
        new_setup = Setup(project_type=template_to_copy.setup.project_type,
                      sample_prep_method=template_to_copy.setup.sample_prep_method)
    else:
        new_setup = Setup()
    new_setup.save()
    #Copy Content
    if template_to_copy.content is not None:
        new_content = Content(experiment_goal=template_to_copy.content.experiment_goal,
                          experiment_desc=template_to_copy.content.experiment_desc,
                          experiment_focus=template_to_copy.content.experiment_focus)
    else:
        new_content = Content()
    new_content.save()
    #Create project
    new_project = Project(project_name=project_name,
                          is_template=False,
                          information=new_info,
                          setup=new_setup,
                          content=new_content)
    new_project.save()
    # Copy devices
    if template_to_copy.setup.devices_names is not None:
        for device in template_to_copy.setup.devices_names.all():
            new_device = DeviceNames(name=device.name, is_reference=device.is_reference)
            new_device.save()
            new_project.setup.devices_names.add(new_device)
    # Copy sequences
    if template_to_copy.setup.seq_def is not None:
        for sequ in template_to_copy.setup.seq_def.all():
            new_seq = Sequences(name=sequ.name, sample_matrix=sequ.sample_matrix, sample_type=sequ.sample_type)
            new_seq.save()
            for seq_def in sequ.seq.all():
                new_seq_def = SequenceDefinition(order_number=seq_def.order_number,
                                                 param=seq_def.param,
                                                 level=seq_def.level,
                                                 pause_time=seq_def.pause_time,
                                                 break_def=seq_def.break_def)
                new_seq_def.save()
                new_seq.seq.add(new_seq_def)
            new_seq.save()
            new_project.setup.seq_def.add(new_seq)
        new_project.save()
    # Copy lvls
    if template_to_copy.setup.levels is not None:
        for lvl in template_to_copy.setup.levels.all():
            new_lvl = Levels(param=lvl.param)
            new_lvl.save()
            for lvldef in lvl.lvl_def.all():
                new_lvl_def = LevelDefinition(lvl_nbr=lvldef.lvl_nbr,
                                              measurement_nbr=lvldef.measurement_nbr,
                                              target_value=lvldef.target_value,
                                              acceptance_criteria=lvldef.acceptance_criteria)
                new_lvl_def.save()
                new_lvl.lvl_def.add(new_lvl_def)
            new_lvl.save()
            new_project.setup.levels.add(new_lvl)
        new_project.save()
    return new_project.id