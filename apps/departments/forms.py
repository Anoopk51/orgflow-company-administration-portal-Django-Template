from django import forms

from .models import Department
from apps.employees.models import Employee


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = [
            "name",
            "code",
            "description",
            "head",
        ]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["head"].queryset = Employee.objects.all()