from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render , redirect
from .models import Employee , EmployeeStatus
from apps.accounts.models import Role
from .forms import CreateEmployeeForm , EmployeeProfileUpdateForm
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

#  This is for employee_list it is only for admin and superadmin accessiable

@login_required
def employee_list(request):

    if request.user.role not in [
        Role.SUPER_ADMIN,
        Role.ADMIN,
    ]:
        return HttpResponseForbidden(
            "You are not allowed to view employees."
        )

    employees = Employee.objects.select_related("user", "department", "manager",).all()

    return render(
        request,
        "employees/employee_list.html",
        {"employees": employees},
    )

# this is employee details it only for visibale for super admin , admin and employee it self.
@login_required
def employee_detail(request,employee_id):

    if request.user.role not in [Role.SUPER_ADMIN ,Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to view employee details.")

    employee  = get_object_or_404(
        Employee.objects.select_related("user","department","manager",),
        employee_id = employee_id,
    )

    return render(request,"employees/employee_detail.html",{"employee":employee},)

# For employee cannot access their own profile.

@login_required
def my_profile(request):

    employee = get_object_or_404(
        Employee.objects.select_related("user","department","manager",),user = request.user,
        )
    return render(request,"employees/my_profile.html",{"employee":employee},)

# This is for view -- update employee

@login_required
def update_employee(request,employee_id):

    employee = get_object_or_404(Employee.objects.select_related("user","department","manager",),employee_id = employee_id,)

    if request.user.role  in [Role.SUPER_ADMIN ,Role.ADMIN]:
        allowed = True

    elif(request.user.role == Role.EMPLOYEE and employee.user == request.user):
        allowed =  True

    else:
        allowed = False

    if not allowed:
        return HttpResponseForbidden("You are not allowed to update this employee.")

    if request.method == "POST":
        form  = CreateEmployeeForm(request.POST ,request.FILES,instance = employee,)

        if form.is_valid():
            form.save()

            return redirect("employee_detail",employee_id=employee.employee_id,)

    else:
        form = CreateEmployeeForm(instance = employee)

    return render(request,"employees/update_employee.html",{"form":form,"employee":employee,},)

# This is for employee status for deactivate employee handle feature.

@login_required
def deactivate_employee(request,employee_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.SUPER_ADMIN,]:
        return HttpResponseForbidden("You are not allowed to deactivate employees.")

    employee = get_object_or_404(Employee.objects.select_related("user"),employee_id=employee_id,)

    if request.method == "POST":
        employee.status = EmployeeStatus.RESIGNED
        employee.user.is_active = False

        employee.save(update_fields=["status","updated_at"])
        employee.user.save(update_fields=["is_active"])

        return redirect("employee_detail",employee_id = employee.employee_id,)

    return render(request,"employees/deactivate_employee.html",{"employee":employee},)


# this is for self file update.
@login_required
def update_my_profile(request):

    employee = get_object_or_404(
        Employee,
        user=request.user,
    )

    if request.method == "POST":
        form = EmployeeProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=employee,
        )

        if form.is_valid():
            form.save()

            return redirect("my_profile")

    else:
        form = EmployeeProfileUpdateForm(
            instance=employee,
        )

    return render(
        request,
        "employees/update_my_profile.html",
        {"form": form},
    )