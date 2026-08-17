from django.urls import path

from .views import create_task , task_list , task_detail ,update_task , delete_task

urlpatterns = [
    path("tasks/",task_list,name = "task_list",),
    path("tasks/create/",create_task,name="create_task",),
    path("tasks/<int:task_id>/,",task_detail,name = "task_detail",),
    path("tasks/<int:task_id>/edit/",update_task,name="update_task",),
    path("tasks/<int:task_id>/delete/",delete_task,name="delete_task",),
]

