from django.urls import path, include
from django.conf.urls import url
from . import views

"""
    Url pattern.
    Mainly use "path": path('path', view.to.connect)

    url can also be used (see on documentation)

    this class is included in the main urls file (OPIA/urls.py)
"""

urlpatterns = [
    path('', views.home),
    url(r'^login', views.connection, name='login'),
    url(r'^deconnect', views.deconnection, name='deconnection'),
    url(r'^admin_home', views.admin_home, name='admin_home'),
]