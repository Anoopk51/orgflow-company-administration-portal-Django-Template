from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.http import HttpResponseForbidden

from .forms import CreateUserForm
from .models import Role ,User
# Create your views here.

def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request,username = email,password = password, )

        if user is not None:
            login(request , user)
            return redirect("dashboard")

        return render(request,"accounts/login.html",{"error":"Invalid email or password." },)

    return render(request , "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def create_user(request):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to create users.")


    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            User.objects.create_user(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                role = form.cleaned_data["role"],
            )

            return redirect("dashboard")
    else:
        form = CreateUserForm()

    return render(request,"accounts/create_user.html",{"form":form},)
    
    
