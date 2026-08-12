from django.urls import path

from .views import create_employee ,employee_list , employee_detail

urlpatterns = [
    path("employees/",employee_list,name="employee_list",),
    path("employees/create/",create_employee,name="create_employee",),
    path("employee/<str:employee_id>/",employee_detail,name="employee_detail",),
]
                        