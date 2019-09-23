from django.urls import path
from . import views

"""
    Url pattern.
    Mainly use "path": path('path', view.to.connect)
    
    url can also be used (see on documentation)
    
    this class is included in the main urls file (OPIA/urls.py)
"""

urlpatterns = [
    path('home', views.home),

    path('year', views.year),
    path('sprint', views.sprint),
    path('wiki', views.wiki),
    path('todo', views.todo),
    path('article', views.article),
    path('articl/create', views.article_create),
    path('articledef/<int:articleid>', views.articledef),
    path('dashboard', views.dashboard),
    path('mgmt', views.mgmt),
    path('sprint/def/<int:sprint_id>', views.sprint_def),
    path('rapport/<int:sprint_id>/<int:rapport_id>', views.rapport_def),
    path('rapport/create/<int:sprint_id>/<int:part_id>', views.rapport_create),





    path('dataov', views.dataoverview),

    #use this for each project
    #only for tests purpose
    path('projecttest/<int:year>/', views.project_testview),
    path('projecttest/<int:year>/<int:month>', views.project_testview),
    path('redirect', views.view_redirected),
    path('date', views.date_actuelle),
]