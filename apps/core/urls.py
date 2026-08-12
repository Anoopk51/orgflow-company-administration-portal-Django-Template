from django.urls import path
from .views import dashboard
from apps.accounts.views import create_user

urlpatterns = [
    path("dashboard/",dashboard,name="dashboard",),

    path("dashboard/users/create/",create_user,name= "create_user",),
]
