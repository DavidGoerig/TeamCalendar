from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from datetime import datetime
from django.db import IntegrityError

from .models import Sprint, Part, KnowledgeArticle, Rapport, WikiArticle, Meeting, Task, Todo, GroupTask
from .forms import MeetingForm, RapportForm, TaskForm, TodoForm, KnowledgeArticleForm, GrouptaskForm, WikiArticleForm

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
    domainstring = "/"
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
    wikis = WikiArticle.objects.all()
    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "delit":
            WikiArticle.objects.get(id=id[1]).delete()
            return HttpResponseRedirect('/cal/wiki')
        if id[0] == "addone":
            form = WikiArticleForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/cal/wiki')
    form = WikiArticleForm(None)
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
    todos = Todo.objects.all()
    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "addtask":
            todo = Todo.objects.get(id=id[1])
            taskform = TaskForm(request.POST)
            if taskform.is_valid():
                new = taskform.save()
                todo.todo.add(new)
            taskform = TaskForm()
            return HttpResponseRedirect('/cal/todo')
        elif id[0] == "deltask":
            Task.objects.get(id=id[1]).delete()
            return HttpResponseRedirect('/cal/todo')
        elif id[0] == "addtodo":
            todoform = TodoForm(request.POST)
            if todoform.is_valid():
                new = todoform.save()
            todoform = TodoForm()
            return HttpResponseRedirect('/cal/todo')
        elif id[0] == "deltodo":
            Todo.objects.get(id=id[1]).delete()
            return HttpResponseRedirect('/cal/todo')
        elif id[0] == "toggleit":
            task = Task.objects.get(id=id[1])
            boolean = True
            if id[2] == "True":
                boolean = False
            task.is_done = boolean
            task.save()
            return HttpResponseRedirect('/cal/todo')

    todoform = TodoForm()
    taskform = TaskForm()
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
    software = KnowledgeArticle.objects.filter(field="SOFTWARE")
    hardware = KnowledgeArticle.objects.filter(field="HARDWARE")
    front = KnowledgeArticle.objects.filter(field="FRONT END WEB")
    back = KnowledgeArticle.objects.filter(field="BACK END WEB")
    ia = KnowledgeArticle.objects.filter(field="IA")
    management = KnowledgeArticle.objects.filter(field="MANAGEMENT")
    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "delit":
            KnowledgeArticle.objects.get(id=id[1]).delete()
            return HttpResponseRedirect('/cal/article')
    return render(request, 'calendar/article.html', locals())

"""
    This function define the page: article

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/article.html
"""
@login_required
def articledef(request, articleid):
    default = "article"
    try:
        article = KnowledgeArticle.objects.get(id=articleid)
    except Sprint.DoesNotExist:
        article = None
    if article == None:
        raise Http404
    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "delarticle":
            article.delete()
    form = KnowledgeArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/cal/articledef/' + str(articleid))
    return render(request, 'calendar/article_def.html', locals())

@login_required
def article_create(request):
    new_article = KnowledgeArticle()
    new_article.save()
    return redirect('/cal/articledef/' + str(new_article.id))

"""
    This function define the page: dashboard

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: calendar/dashboard.html
"""
@login_required
def dashboard(request):
    david = GroupTask.objects.filter(assigned_member="David")
    hamid = GroupTask.objects.filter(assigned_member="Hamid")
    guillaume = GroupTask.objects.filter(assigned_member="Guillaume")
    none = GroupTask.objects.filter(assigned_member="None")
    william = GroupTask.objects.filter(assigned_member="William")
    florian = GroupTask.objects.filter(assigned_member="Florian")
    rodolphe = GroupTask.objects.filter(assigned_member="Rodolphe")
    for iteration in request.POST:
        id = iteration.split(":", 3)
        if id[0] == "unassign":
            groupast = GroupTask.objects.get(id=id[1])
            groupast.assigned_member = "None"
            groupast.save()
            return HttpResponseRedirect('/cal/dashboard')
        if id[0] == "assign":
            groupast = GroupTask.objects.get(id=id[1])
            groupast.assigned_member = id[2]
            groupast.save()
            return HttpResponseRedirect('/cal/dashboard')
        if id[0] == "addone":
            form = GrouptaskForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/cal/dashboard')
        if id[0] == "delit":
            GroupTask.objects.get(id=id[1]).delete()
            return HttpResponseRedirect('/cal/dashboard')

    form = GrouptaskForm(None)
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
        print(id)
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
        elif id[0] == "exporttxt":
            part = Part.objects.get(id=id[1])
            content = ""
            rapports = part.rapport_mensuel.all()
            for rapport in rapports:
                content = content + rapport.auteur + ":\n" +  rapport.descriptif_done + "\n\n"
            filename = "rapport.txt"
            response = HttpResponse(content, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            return response
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
##################################################################################################################
#                             This are only tests views (aim to be deleted)                                      #
##################################################################################################################

def project_testview(request, year, month=None):
    return HttpResponse('Project nr %s %s' % (year, month))

def view_redirected(request):
    return HttpResponse("Redirected!")

def date_actuelle(request):
    return render(request, 'labtesting/date.html', {'date': datetime.now()})
