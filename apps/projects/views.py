from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render , redirect ,get_object_or_404

from apps.accounts.models import Role
from .forms import ProjectForm
from .models import Project

# Create your views here.

# This is for createing project by admin and superadmin.
@login_required
def create_project(request):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to create project.")

    if request.method == "POST":

        form =ProjectForm(request.POST)

        if form.is_valid():
            project = form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request,"projects/create_project.html",{"form":form},)


# This is for project listing
@login_required
def project_list(request):

    if request.user.role not in [Role.ADMIN,Role.SUPER_ADMIN]:
        return HttpResponseForbidden("You are not allowed to view projects.")

    projects = Project.objects.prefetch_related("teams",).select_related("project_manager",).all()

    return render(request,"projects/project_list.html",{"projects":projects},)


# This is for project details

@login_required
def project_detail(request,project_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to view project details.")

    project = get_object_or_404(
        Project.objects.select_related("project_manager",).prefetch_related("teams",), id = project_id, )

    return render(request,"projects/project_detail.html",{"project":project},)

# This is for update/edit view  
@login_required
def update_project(request,project_id):

    if request.user.role not in [Role.SUPER_ADMIN ,Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to update projects.")

    project = get_object_or_404(Project , id = project_id,)

    if request.method == "POST":
        form =ProjectForm(request.POST,instance = project,)

        if form.is_valid():
            form.save()

            return redirect("project_detail",project_id=project.id,)
    else:
        form =ProjectForm(instance = project,)

    return render(request,"projects/update_project.html",{"form":form,"project":project,},)

# For project activate or deactivate ke liye
@login_required
def deactivate_project(request,project_id):

    if request.user.role not in [Role.ADMIN,Role.SUPER_ADMIN]:
        return HttpResponseForbidden("You are not allow to activate deactivate projects.")

    project = get_object_or_404(Project,id = project_id)

    if request.method == "POST":

        project.is_active = False

        project.save(update_fields=['is_active','updated_at'])

        return redirect("project_detail",project_id = project.id,)
    return render(request,"projects/deactivate_project.html",{"project":project},)


# This is for activate project purpose

@login_required
def activate_project(request,project_id):

    if request.user.role not in [Role.SUPER_ADMIN,Role.ADMIN]:
        return HttpResponseForbidden("Yor are not allowed to activate projects.")

    project = get_object_or_404(Project,id = project_id,)

    if request.method == "POST":

        project.is_active = True

        project.save(update_fields=['is_active','updated_at'])

        return redirect("project_detail",project_id = project.id,)
    return render(request,"projects/activate_project.html",{"project":project},)
    