from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ConnexionForm

# Create your views here.

"""
    This function define the home of the cir part

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: homensettings/home.html
"""
@login_required
def home(request):
    name = request.user.username
    return render(request, 'homensettings/home.html', locals())


"""
    This function create the page for the connection.
    If the request method is POST (so the form return), it try to authenticate the user and if it works redirect to the home.
    Otherwise it display the form

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: homensettings/login.html
        or
        redirection to home page
"""
def connection(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # are the information correct?
            if user:  # if the object isnt None
                login(request, user)  # we need to connect the user
                return redirect(home)
            else:  # otherwise display an error
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'homensettings/login.html', locals())

"""
    This function is used to disconnect the user

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        redirection to connection page
"""
def deconnection(request):
    logout(request)
    return redirect("/login/?next=/")

"""
    This function is used to create the administration home

    Args:
        request: object containing view information (GET, POST, temp variables, etc).

    Returns:
        render: with local variables and a link to the template: homensettings/admin_home.html
"""
@login_required
def admin_home(request):
    name = request.user.username
    return render(request, 'homensettings/admin_home.html', locals())
