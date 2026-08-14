from django.urls import path

from .views import create_project ,project_list , project_detail , update_project , deactivate_project ,activate_project

urlpatterns = [
    path("projects/",project_list,name="project_list",),
    path("projects/create/",create_project,name="create_project",),
    path("projects/<int:project_id>/",project_detail,name="project_detail",), 
    path("projects/<int:project_id>/edit/",update_project,name = "update_project",),
    path("projects/<int:project_id>/deactivate/",deactivate_project,name="deactivate_project",),
    path("projects/<int:project_id>/activate/",activate_project,name="activate_project",),
    
]
