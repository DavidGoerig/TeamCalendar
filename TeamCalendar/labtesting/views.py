from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from datetime import datetime
from .forms import ProjectForm, InformationForm, TimelineDaysForm, NameForm, ContentForm, ParametersLevelForm, LevelDefinitionForm, SetupForm, SequenceDefinitionForm, DeviceNamesForm, SequencesForm, ChecksForm
from .models import Project, Setup, Levels, SequenceDefinition, Sequences, TimelineDays

from .settings import *
from .create_project_from_template import *
from django.db import IntegrityError

from .models import Sprint, Part, KnowledgeArticle, Rapport, Article, Meeting
from .forms import MeetingForm, RapportForm

##
##  Each url are defined in the file /labtesting/urls.py
##

"""
    This function define the home of the labtesting part

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: labtesting/home.html
"""
@login_required
def home(request):
    domainstring = "http://localhost:8000/"
    return render(request, 'labtesting/home.html', locals())

"""
    This function define the page: year

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/year.html
"""
@login_required
def year(request):
    default = "Year"
    sprints = Sprint.objects.all()
    meetings = Meeting.objects.all()
    parts = Part.objects.all()
    #Rajouter la date d'aujourd'hui avec le truc python
    #Boucler d'abord dans les sprints, puis dans les parties pe????
    return render(request, 'calendar/year.html', locals())


"""
    This function define the page: sprint

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/sprint.html
"""
@login_required
def sprint(request):
    default = "Sprint"
    sprints = Sprint.objects.all()
    current = 3
    return render(request, 'calendar/sprint.html', locals())

"""
    This function define the page: wiki

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/wiki.html
"""
@login_required
def wiki(request):
    default = "Wiki"
    return render(request, 'calendar/wiki.html', locals())

"""
    This function define the page: todo

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/todo.html
"""
@login_required
def todo(request):
    default = "todo"
    return render(request, 'calendar/todo.html', locals())

"""
    This function define the page: article

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/article.html
"""
@login_required
def article(request):
    default = "article"
    return render(request, 'calendar/article.html', locals())

"""
    This function define the page: dashboard

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/dashboard.html
"""
@login_required
def dashboard(request):
    default = "dashboard"
    return render(request, 'calendar/dashboard.html', locals())

"""
    This function define the page: mgmt

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/mgmt.html
"""
@login_required
def mgmt(request):
    default = "mgmt"
    return render(request, 'calendar/mgmt.html', locals())

"""
    This function define the page: 

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: 
"""
@login_required
def sprint_def(request, sprint_id):
    try:
        sprint = Sprint.objects.get(id=sprint_id)
    except Sprint.DoesNotExist:
        sprint = None
    if sprint == None:
        raise Http404
    sprint_part = sprint.sprint_part.all()
    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "addevent":
            form = MeetingForm(request.POST)
            if form.is_valid():
                new = form.save()
                part = Part.objects.get(id=id[1])
                part.meetings.add(new)
            return HttpResponseRedirect('/cal/sprint/def/' + str(sprint_id))
        elif id[0] == "delevent":
            Meeting.objects.get(id=id[1]).delete()
            return HttpResponseRedirect('/cal/sprint/def/' + str(sprint_id))
        elif id[0] == "pld":
            part = Part.objects.get(id=id[1])
            boolean = False
            if id[2] == "True":
                boolean = True
            part.is_pld_update = boolean
            part.save()
            return HttpResponseRedirect('/cal/sprint/def/' + str(sprint_id))
        elif id[0] == "rdv":
            part = Part.objects.get(id=id[1])
            boolean = False
            if id[2] == "True":
                boolean = True
            part.is_meeting_ready = boolean
            part.save()
            return HttpResponseRedirect('/cal/sprint/def/' + str(sprint_id))

    form = MeetingForm()
    return render(request, 'calendar/sprint_def.html', locals())


@login_required
def rapport_def(request, sprint_id, rapport_id):
    try:
        rapport = Rapport.objects.get(id=rapport_id)
    except Rapport.DoesNotExist:
        raise Http404
    form = RapportForm(request.POST or None, instance=rapport)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/cal/rapport/' + str(sprint_id) + "/" + str(rapport_id))
    return render(request, 'calendar/rapport.html', locals())


@login_required
def rapport_create(request, sprint_id, part_id):
    try:
        part = Part.objects.get(id=part_id)
    except Part.DoesNotExist:
        part = None
    if part == None:
        raise Http404
    new_rapport = Rapport(auteur="David", descriptif_done="")
    new_rapport.save()
    part.rapport_mensuel.add(new_rapport)
    return redirect('/cal/rapport/' + str(sprint_id) + '/' + str(new_rapport.id))



 #################################################################################################


"""
    This function define the page: test defaults

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: labtesting/default.html
"""
@login_required
def deftest(request):
    title = "Templates projects"
    projects = Project.objects.exclude(is_template=False)
    return render(request, 'labtesting/display_templates.html', locals())

"""
    This function define the page: project planner

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: labtesting/default.html
"""
@login_required
def planproject(request):
    name = None
    projects = Project.objects.exclude(is_template=False)
    form = NameForm(request.POST or None)
    already_used_name = False
    for iteration in request.POST:
        id = iteration.split(":", 2)
        if id[0] == "new_project":
            project = Project(project_name=id[1], is_template=False) # changer toutes les lignes du template et les garder si c'est un nouveau proj (et renommer la variable projet)
            try:
                project.save()
            except IntegrityError:
                already_used_name = True
            if already_used_name is False:
                temp = Setup(project_type="None")
                temp.save()
                project.setup = temp
                project.save()
                return redirect(project_content, project_id=project.id, first_creation=True)
        elif id[0] == "choose_template":
            try:
               id_new_proj = copy_project(id[1], id[2])
            except IntegrityError:
                already_used_name = True
            if already_used_name is False:
                return redirect(project_content, project_id=id_new_proj, first_creation=True)
    if form.is_valid():
        cd = form.cleaned_data
        name = cd.get('name')
    return render(request, 'labtesting/projects_pages/create_project.html', locals())

"""
    This function define the page: schedule

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: labtesting/default.html
"""
@login_required
def schedule(request):
    default = "Schedule page"
    return render(request, 'labtesting/default.html', locals())

"""
    This function define the page: workflow

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: labtesting/default.html
"""
@login_required
def workflow(request):
    title = "Workflow"
    projects = Project.objects.exclude(is_template=True)
    return render(request, 'labtesting/display_projects.html', locals())

"""
    This function define the page: data overview

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: labtesting/default.html
"""
@login_required
def dataoverview(request):
    default = "Data overwiew"
    return render(request, 'labtesting/default.html', locals())

"""
    This function define the project given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/project.html
        404 if this project don't exist
"""
@login_required
def project_view(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    if request.method == 'POST' and ("delete" in request.POST):
        project.delete()
        return redirect("/lab/workflow")
    return render(request, 'labtesting/project.html', locals())

"""
    This function define the project's content given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/content.html
        404 if this project don't exist
"""
@login_required
def project_content(request, project_id, first_creation=False):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    if first_creation is False:
        info_filled = True
    infoform = InformationForm(instance=project.information)
    if request.method == 'POST' and ("addinfo" in request.POST):
        infoform = InformationForm(request.POST, instance=project.information)
    if infoform.is_valid():
        info_filled = True
        info = infoform.save()
        project.information = info
        project.save()
    form = ContentForm(instance=project.content)
    if request.method == 'POST' and ("addcontent" in request.POST):
        form = ContentForm(request.POST, instance=project.content)
    if form.is_valid():
        info_filled = True
        new = form.save()
        project.content = new
        project.save()
    return render(request, 'labtesting/projects_pages/content.html', locals())

"""
    This function define the project given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/project.html
        404 if this project don't exist
"""
@login_required
def project_setup(request, project_id, first_creation=False):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    if project.setup is None:
        temp = Setup(project_type="None")
        temp.save()
        project.setup = temp
        project.save()
    title = "Project Setup"
    levels, levels_disp, device_disp, sequence, sequence_disp, lastid, lvlform, pause_form, form, seqform, proj_form, device_form = settings_main(project, request)
    return render(request, 'labtesting/templates_pages/setup.html', locals())


"""
    This function define the project given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/project.html
        404 if this project don't exist
"""
@login_required
def project_orga(request, project_id, first_creation=False):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    return render(request, 'labtesting/projects_pages/orga.html', locals())




"""
    This function define the project given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/project.html
        404 if this project don't exist
"""
@login_required
def project_meas(request, project_id, first_creation=False):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    timeline = project.timeline
    timeline_disp = timeline.all()
    return render(request, 'labtesting/projects_pages/measurement.html', locals())

def project_measday(request, project_id, day_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    day = project.timeline.get(id=day_id) # faire un try except
    return render(request, 'labtesting/projects_pages/measurement_day.html', locals())

"""
    This function define the project given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/project.html
        404 if this project don't exist
"""
@login_required
def project_checks(request, project_id, first_creation=False):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project is None or project.is_template is True:
        raise Http404
    form = ChecksForm(instance=project.checks)
    if request.method == 'POST' and ("modifychecks" in request.POST):
        form = ChecksForm(request.POST, instance=project.checks)
    if form.is_valid():
        new = form.save()
        project.checks = new
        project.save()
    return render(request, 'labtesting/projects_pages/checks.html', locals())


"""
    This function define the project given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/project.html
        404 if this project don't exist
"""
@login_required
def template_view(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == False:
        raise Http404
    if request.method == 'POST' and ("delete" in request.POST):
        project.delete()
        return redirect("/lab/deftest")
    return render(request, 'labtesting/templates_pages/template.html', locals())

"""
    This function define the project's content given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/content.html
        404 if this project don't exist
"""
@login_required
def template_content(request, project_id, first_creation=False):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == False:
        raise Http404
    if first_creation is False:
        info_filled = True
    infoform = InformationForm(instance=project.information)
    if request.method == 'POST' and ("addinfo" in request.POST):
        infoform = InformationForm(request.POST, instance=project.information)
    if infoform.is_valid():
        info_filled = True
        info = infoform.save()
        project.information = info
        project.save()
    form = ContentForm(instance=project.content)
    if request.method == 'POST' and ("addcontent" in request.POST):
        form = ContentForm(request.POST, instance=project.content)
    if form.is_valid():
        info_filled = True
        new = form.save()
        project.content = new
        project.save()
    return render(request, 'labtesting/templates_pages/content.html', locals())


"""
    This function define the project given in argument

    Args:
        request: object containing view information (GET, POST, temp variables, etc).
        project_id: project id to display.

    Returns:
        render: with local variables and a link to the template: labtesting/project.html
        404 if this project don't exist
"""
@login_required
def template_setup(request, project_id, first_creation=False):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == False:
        raise Http404
    if project.setup is None:
        temp = Setup(project_type="None")
        temp.save()
        project.setup = temp
        project.save()
    title = "Template Setup"
    levels, levels_disp, device_disp, sequence, sequence_disp, lastid, lvlform, pause_form, form, seqform, proj_form, device_form = settings_main(project, request)
    return render(request, 'labtesting/templates_pages/setup.html', locals())

@login_required
def template_create(request):
    form = NameForm(request.POST or None)
    already_used_name = False
    if form.is_valid():
        cd = form.cleaned_data
        name = cd.get('name')
        template = Project(project_name=name, is_template=True)
        try:
            template.save()
        except IntegrityError:
            already_used_name = True
        if already_used_name is False:
            temp = Setup(project_type="None")
            temp.save()
            template.setup = temp
            template.save()
            return redirect(template_content, project_id=template.id, first_creation=True)
    return render(request, 'labtesting/templates_pages/create_template.html', locals())


def project_order(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    return render(request, 'labtesting/organisation_pages/orders.html', locals())

def project_instrument_reservation(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    return render(request, 'labtesting/organisation_pages/instrument_reservation.html', locals())

def project_timeline_creation(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None or project.is_template == True:
        raise Http404
    sequence = project.setup.seq_def
    sequence_disp = project.setup.seq_def.all()

    timeline = project.timeline
    timeline_disp = timeline.all()
    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "chooselevel":
            full_seq = sequence.get(id=id[2])
            sequence_to_modify = full_seq.seq.get(id=id[1])
            day_nbr = 1
            if timeline_disp.count() is not 0:
                day_nbr = timeline.order_by("day_nbr").reverse()[0].day_nbr + 1
            new_day = TimelineDays(day_nbr=day_nbr,
                                   seq_name=full_seq.name,
                                   lvl_nbr=sequence_to_modify.level,
                                   param=sequence_to_modify.param,
                                   sample_type=full_seq.sample_type,
                                   sample_matrix=full_seq.sample_matrix,
                                   pause_time=sequence_to_modify.pause_time,
                                   break_def=sequence_to_modify.break_def)
            new_day.save()
            timeline.add(new_day)
            project.save()
        elif id[0] == "add_full_seq":
            sequence_full = sequence.get(id=id[1])
            seq_name = sequence_full.name
            seq_sample_type = sequence_full.sample_type
            seq_sample_matrix = sequence_full.sample_matrix
            for seq in sequence_full.seq.all():
                day_nbr = 1
                if timeline_disp.count() is not 0:
                    day_nbr = timeline.order_by("day_nbr").reverse()[0].day_nbr + 1
                new_day = TimelineDays(day_nbr=day_nbr,
                                       seq_name=seq_name,
                                       lvl_nbr=seq.level,
                                       param=seq.param,
                                       sample_type=seq_sample_type,
                                       sample_matrix=seq_sample_matrix,
                                       pause_time=seq.pause_time,
                                       break_def=seq.break_def)
                new_day.save()
                timeline.add(new_day)
            project.save()
        elif id[0] == "deletetimelineday":
            timelineday_to_del = timeline.get(id=id[1])
            day_nbr_del = timelineday_to_del.day_nbr
            timelineday_to_del.delete()
            for day in timeline_disp:
                if day.day_nbr > day_nbr_del:
                    day.day_nbr = day.day_nbr - 1
                    day.save()



    return render(request, 'labtesting/organisation_pages/timeline_creation.html', locals())

##################################################################################################################
#                             This are only tests views (aim to be deleted)                                      #
##################################################################################################################

def project_testview(request, year, month=None):
    return HttpResponse('Project nr %s %s' % (year, month))

def view_redirected(request):
    return HttpResponse("Redirected!")

def date_actuelle(request):
    return render(request, 'labtesting/date.html', {'date': datetime.now()})

def testview(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None:
        raise Http404
    form = ProjectForm(instance=project)

    if request.method == 'POST' and ("form1" in request.POST):
        form = ProjectForm(request.POST, instance=project)
    if form.is_valid():
        envoi = True
        form.save()
    infoform = InformationForm(instance=project.information)
    if request.method == 'POST' and ("form2" in request.POST):
        infoform = InformationForm(request.POST, instance=project.information)
    if infoform.is_valid():
        envoi = True
        infoform.save()
    return render(request, 'labtesting/contact.html', locals())

def testviewform(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        project = None
    if project == None:
        raise Http404
    for iteration in request.POST:
        id = iteration.split(":", 1)
        if id[0] == "delete":
            print(id[1])
            project.timeline.get(id=id[1]).delete()
    timeline = project.timeline
    alltimeline = project.timeline.all()
    form = TimelineDaysForm(None)
    if request.method == 'POST' and ("adddays" in request.POST):
        form = TimelineDaysForm(request.POST or None)
    if form.is_valid():
        new_day = form.save()
        timeline.add(new_day)
        form = TimelineDaysForm(None)
    return render(request, 'labtesting/testpurposeTODELETE.html', locals())
