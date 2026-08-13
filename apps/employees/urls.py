from django.urls import path

from .views import create_employee ,employee_list , employee_detail ,my_profile , update_employee , deactivate_employee , update_my_profile

urlpatterns = [
    path("employees/",employee_list,name="employee_list",),
    path("employees/create/",create_employee,name="create_employee",),
    path("employee/<str:employee_id>/",employee_detail,name="employee_detail",),
    path("employee/<str:employee_id>/edit/",update_employee,name ="update_employee",),
    path("employee/<str:employee_id>/deactivate/",deactivate_employee,name="deactivate_employee",),
    path("profile/",my_profile,name = 'my_profile',),
    path("profile/edit/",update_my_profile,name="update_my_profile",),
]
                        