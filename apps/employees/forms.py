from django import forms

from .models import Employee
from apps.accounts.models import User

class CreateEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            "user",
            "department",
            "manager",
            "joining_date",
            "status",
            "phone_number",
            "profile_photo",
            "date_of_birth",
        ]

        widgets =  {
            "joining_date": forms.DateInput(attrs={"type":"date"}) , "date_of_birth":forms.DateInput(attrs={"type":"date"}),
        }


    def __init__(self,*args, **kwargs):
        super().__init__(*args , **kwargs)

        # Only Users who don't already have an employee profile.
        self.fields["user"].queryset = User.objects.filter(
            employee_profile__isnull = True
        )

        # Only existing employees can be selected as managers
        self.fields["manager"].queryset = Employee.objects.all()