from django.urls import path
from .views import create_team , team_list , team_detail , update_team , deactivate_team , activate_team , manage_team_members

urlpatterns = [
  
    path("teams/",team_list,name= "team_list",),
    path("teams/create/",create_team,name="create_team",),
    path("teams/<int:team_id>/",team_detail,name="team_detail",),
    path("teams/<int:team_id>/edit/",update_team,name= "update_team",),
    path("teams/<int:team_id>/deactivate/",deactivate_team,name="deactivate_team",),
    path("teams/<int:team_id>/activate/",activate_team,name="activate_team",),
    path("teams/<int:team_id>/members/",manage_team_members,name="manage_team_members",),

]
