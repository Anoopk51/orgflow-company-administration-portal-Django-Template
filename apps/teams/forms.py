from django import forms 

from .models import Team
from apps.employees.models import Employee

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team

        fields = ["name","department","leader","description",]

    def __init__(self , *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['leader'].queryset = Employee.objects.all()


class TeamMembersForm(forms.Form):

    """
    Because one team can contain multiple employees.
    """
    members = forms.ModelMultipleChoiceField(queryset=Employee.objects.all(),
                                             widget = forms.CheckboxSelectMultiple,
                                             required = False,)