from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render , redirect , get_object_or_404

from apps.accounts.models import Role
from .forms import DepartmentForm
from .models import Department

# Create your views here.

# This is just a creating for department 
@login_required
def create_department(request):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN,]:
        return HttpResponseForbidden(
            "You are not allowed to create departments."
        )

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm()

    return render(request,"departments/create_department.html",{"form":form},)


# This is just a show the department list 

@login_required
def department_list(request):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to view departments.")


    departments= Department.objects.select_related("head",).all()

    return render(request,"departments/department_list.html",{"departments":departments},)

# For departments details overview

@login_required
def department_detail(request,department_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to view departments.")

    department = get_object_or_404(Department.objects.select_related("head"),id = department_id,)

    employees = department.employees.select_related("user", "manager",).all()

    return render(request,"departments/department_detail.html", {"department":department,"employees":employees,},)

 # It's for add update and view

@login_required
def update_department(request,department_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to update departments.")

    department = get_object_or_404(Department,id = department_id, )

    if request.method == "POST":

        form = DepartmentForm(request.POST,instance=department,)

        if form.is_valid():
            form.save()
            return redirect("department_detail",department_id = department.id,)

    else:
        form  = DepartmentForm(instance = department,)
    return render(request,"departments/update_department.html",{"form":form,"department":department,},)
    
# for deactivate departments

@login_required
def deactivate_department(request,department_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to deactivate departments.")

    department = get_object_or_404(Department,id = department_id,)

    if request.method == "POST":
        department.is_active = False
        department.save(update_fields=['is_active','updated_at'])

        return redirect("department_detail",department_id=department.id,)

    return render(request,"departments/deactivate_department.html",{"department":department},)

@login_required
def activate_department(request,department_id):

    if request.user.role not in [Role.SUPER_ADMIN,Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to activate departments.")

    department = get_object_or_404(Department,id = department_id,)

    if request.method == "POST":
        department.is_active = True
        department.save(
            update_fields=["is_active","updated_at"]
        )
        return redirect("department_detail",department_id=department.id,)

    return render(request,"departments/activate_department.html",{"department":department},)
