from django.urls import path

from .views import create_department , department_list , department_detail , update_department ,deactivate_department , activate_department
 
urlpatterns = [
    path("departments/",department_list,name="department_list",),
    path("departments/create/",create_department,name="create_department",),
    path("departments/<int:department_id>/",department_detail,name="department_detail",),
    path("departments/<int:department_id>/edit/",update_department,name = "update_department",),
    path("departments/<int:department_id>/deactivate/",deactivate_department,name="deactivate_department",),
    path("departments/<int:department_id>/activate/",activate_department,name="activate_department",),
]