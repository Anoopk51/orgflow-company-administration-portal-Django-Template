from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render , redirect
from .models import Employee
from apps.accounts.models import Role
from .forms import CreateEmployeeForm
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def create_employee(request):

    # Authorization
    if request.user.role not in [Role.SUPER_ADMIN, Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to create employee profiles.")


    if request.method == "POST":

        form  = CreateEmployeeForm(request.POST , request.FILES)

        if form.is_valid():

            employee = form.save(commit=False)

            last_employee = (
                Employee.objects.order_by("-id").first()
                             )

            if last_employee:
                next_number = last_employee.id + 1
            else:
                next_number = 1
                
            employee.employee_id = f"EMP{next_number:03d}"

            employee.save()

            return redirect("dashboard")

    else:
        form = CreateEmployeeForm()

    return render(request,"employees/create_employee.html",{"form":form},)

@login_required
def employee_list(request):

    if request.user.role not in [
        Role.SUPER_ADMIN,
        Role.ADMIN,
    ]:
        return HttpResponseForbidden(
            "You are not allowed to view employees."
        )

    employees = Employee.objects.select_related(
        "user",
        "department",
        "manager",
    ).all()

    return render(
        request,
        "employees/employee_list.html",
        {"employees": employees},
    )

@login_required
def employee_detail(request,employee_id):

    if request.user.role not in [Role.SUPER_ADMIN ,Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to view employee details.")

    employee  = get_object_or_404(
        Employee.objects.select_related("user","department","manager",),
        employee_id = employee_id,
    )

    return render(request,"employees/employee_detail.html",{"employee":employee},)