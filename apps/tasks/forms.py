from django import forms 

from .models import Task
from apps.projects.models import Project
from apps.employees.models import Employee

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = ["title","description",'project','assigned_to','status','priority','due_date',]

        widgets = {
            "due_date":forms.DateInput(attrs  ={'type':'date'}),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["project"].queryset = (Project.objects.filter(is_active = True))

        self.fields["assigned_to"].queryset = (Employee.objects.all())

    def clean_due_date(self):

        due_date = self.cleaned_data.get("due_date")
        project = self.cleaned_data.get("project")

        if due_date and project:

            if due_date < project.start_date:
                raise forms.ValidationError("Task due date cannot be before the project start date.")

            if project.end_date and due_date>project.end_date:
                raise forms.ValidationError("Task due date connot be after the project end date.")
        return due_date
                

class TaskStatusForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["status"]

    
