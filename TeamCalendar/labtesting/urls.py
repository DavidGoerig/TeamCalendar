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
    path('deftest', views.deftest),
    path('planproj', views.planproject),
    path('schedule', views.schedule),
    path('workflow', views.workflow),
    path('dataov', views.dataoverview),

    #use this for each project
    path('project/<project_id>', views.project_view),

    path('project/content/<project_id>/<first_creation>', views.project_content),
    path('project/setup/<project_id>', views.project_setup),
    path('project/orga/<project_id>', views.project_orga),
    path('project/checks/<project_id>', views.project_checks),
    path('project/meas/<project_id>', views.project_meas),
    path('project/measday/<project_id>/<day_id>', views.project_measday),

    # project organisation

    path('project/orga/instrument_reservation/<project_id>', views.project_instrument_reservation),
    path('project/orga/orders/<project_id>', views.project_order),
    path('project/orga/timeline/<project_id>', views.project_timeline_creation),

    #use this for each template
    path('template/view/<project_id>', views.template_view),

    path('template/create', views.template_create),

    path('template/content/<project_id>', views.template_content),
    path('template/setup/<project_id>', views.template_setup),
    path('template/content/<project_id>/<first_creation>', views.template_content),
    path('template/setup/<project_id>/<first_creation>', views.template_setup),

    #only for tests purpose
    path('projecttest/<int:year>/', views.project_testview),
    path('projecttest/<int:year>/<int:month>', views.project_testview),
    path('redirect', views.view_redirected),
    path('date', views.date_actuelle),
    path('testview/<project_id>', views.testview),
    path('testviewform/<project_id>', views.testviewform),
]