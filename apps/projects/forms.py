from django import forms

from .models import Project
from apps.employees.models import Employee
from apps.teams.models import Team


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = ["name","code","description","project_manager","teams","start_date","end_date","status",]

        widgets = {
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "end_date":forms.DateInput(attrs={"type":"date"}),
        }


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["project_manager"].queryset = (Employee.objects.all())

        self.fields["teams"].queryset = (Team.objects.filter(is_active = True))
