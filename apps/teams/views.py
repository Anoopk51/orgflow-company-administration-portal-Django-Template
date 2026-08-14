from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render ,redirect ,get_object_or_404

from apps.accounts.models import Role
from .forms import TeamForm , TeamMembersForm
from .models import Team

# Create your views here.
# This is creating the team
@login_required
def create_team(request):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to create teams.")

    if request.method == "POST":
   
        form = TeamForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("team_list")
    else:
        form = TeamForm()
    return render(request,"teams/create_team.html",{"form":form},)

# This is provide the team_list

@login_required
def team_list(request):

    if request.user.role not in [Role.SUPER_ADMIN ,  Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to view teams.")

    teams = Team.objects.select_related("department","leader",).all()

    return render(request,"teams/team_list.html",{"teams":teams},)

# This is for teams detail work

@login_required
def team_detail(request , team_id):

    if request.user.role not in [Role.SUPER_ADMIN,Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to view team details.")

    team = get_object_or_404(Team.objects.select_related("department","leader",),id = team_id,)
    return render(request,"teams/team_detail.html",{"team":team},)

# This is for update and edit purpose only
@login_required
def update_team(request,team_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to update teams.")

    team = get_object_or_404(Team ,id = team_id,)

    if request.method == "POST":

        form = TeamForm(request.POST,instance = team,)

        if form.is_valid():
            form.save()

            return redirect("team_detail",team_id = team.id,)

    else:
        form = TeamForm(instance = team,)

    return render(request,'teams/update_team.html',{'form':form ,"team":team,},)

# This view just simpaly deactivate

@login_required
def deactivate_team(request , team_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to deactivate teams.")

    team = get_object_or_404(Team, id = team_id,)

    if request.method == "POST":
        team.is_active = False

        team.save(update_fields=['is_active' ,'update_at'])

        return redirect("team_detail",team_id = team.id,)
    return render(request,"teams/deactivate_team.html",{"team":team},)


# This is for acivate teams by admin and super admin.

@login_required
def activate_team(request,team_id):

    if request.user.role not in [Role.SUPER_ADMIN, Role.ADMIN]:
        return HttpResponseForbidden("You are not allowed to activate teams.")

    team = get_object_or_404(Team , id =team_id,)

    if request.method == "POST":
        team.is_active = True

        team.save(update_fields=['is_active','update_at'])

        return redirect("team_detail",team_id = team.id,)
    return render(request,"teams/activate_team.html",{"team":team},)


# this is for manage team members it means add member , view members remove members
@login_required
def manage_team_members(request,team_id):

    if request.user.role not in [Role.SUPER_ADMIN , Role.ADMIN,]:
        return HttpResponseForbidden("You are not allowed to manage team members.")

    team = get_object_or_404(Team , id = team_id,)

    if request.method == "POST":

        form = TeamMembersForm(request.POST)

        if form.is_valid():
            team.members.set(form.cleaned_data["members"])

            return redirect("team_detail",team_id = team.id,)

    else:
        form = TeamMembersForm(
            initial={
                "members":team.members.all()
            }
        )
    return render(request,"teams/manage_team_members.html",{"team":team ,"form":form,},)