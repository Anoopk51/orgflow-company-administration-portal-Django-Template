from django.urls import path
from .views import login_view ,logout_view, create_user

urlpatterns = [
    path("login/",login_view,name="login"),
    path("logout/",logout_view,name="logout"),
    path("users/create/",create_user , name = "create_user"),
]
