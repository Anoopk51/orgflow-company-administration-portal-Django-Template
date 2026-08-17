from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render ,redirect , get_object_or_404

from apps.accounts.models import Role
from .forms import TaskForm ,TaskStatusForm
from .models import Task

# Create your views here.

@login_required
def create_task(request):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to create tasks.")

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request,"tasks/create_task.html",{"form":form},)

# This is for veiw the task list

@login_required
def task_list(request):

    if request.user.role  in [Role.ADMIN , Role.SUPER_ADMIN]:
       tasks = Task.objects.select_related("project","assigned_to",).all()

    elif request.user.role == Role.EMPLOYEE:
        tasks = Task.objects.select_related("project","assigned_to",).filter(assigned_to__user = request.user)
    else:
        return HttpResponseForbidden("You are not allowed to view tasks.")
    
    return render(request,"tasks/task_list.html",{"tasks":tasks},)


# This is task details 

def task_detail(request,task_id):

    task = get_object_or_404(Task.objects.select_related("project","assigned_to",),id = task_id,)

    if request.user.role in  [Role.SUPER_ADMIN , Role.ADMIN,]:
        pass

    elif request.user.role == Role.EMPLOYEE:

        if not task.assigned_to:
            return HttpResponseForbidden("You are not allowed to view this task.")

        if task.assigned_to.user != request.user:
            return HttpResponseForbidden("You are not allowed to view this task.")

    else:
        return HttpResponseForbidden("You are not allowed to view this task.")
    
    return render(request,"tasks/task_detail.html",{"task":task},)

# this is update tasks by admin and super admin.

@login_required
def update_task(request,task_id):

    task = get_object_or_404(Task, id = task_id,)

    # Admin/Super admin
    if request.user.role  in [Role.SUPER_ADMIN , Role.ADMIN]:

        if request.method == "POST":

            form = TaskForm(request.POST,instance = task,)

            if form.is_valid():
                form.save()
                return redirect("task_detail",task_id = task.id,)

        else:
            form = TaskForm(instance= task,)

        return render(request,"tasks/update_task.html",{"form":form, "task":task,},)
    
    # Employee
    elif request.user.role == Role.EMPLOYEE:
        if(task.assigned_to is None or task.assigned_to.user != request.user):
            return HttpResponseForbidden("You are not allowed to update this task.")

        if request.method == "POST":

            form = TaskStatusForm(request.POST,instance=task,)

            if form.is_valid():
                form.save()
                return redirect("task_detail",task_id=task.id,)
        else:
            form = TaskStatusForm(instance=task,)
        return render(request,"tasks/update_task.html",{"form":form,"task":task,},)

    else:
        return HttpResponseForbidden("You are not allowed to update tasks.")
# This is for delete the task

@login_required
def delete_task(request,task_id):

    if request.user.role not in  [Role.SUPER_ADMIN,Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to delete tasks.")

    task =get_object_or_404(Task , id = task_id,)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request,"tasks/delete_task.html",{"task":task,},)

    
    
    

