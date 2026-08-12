from django import forms
from .models import Role


class CreateUserForm(forms.Form):

    email = forms.EmailField()

    first_name = forms.CharField(
        max_length=150,
    )

    last_name = forms.CharField(
        max_length=150,
    )

    role = forms.ChoiceField(
        choices=Role.choices,
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput,
    )

    confirm_password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput,
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match."
            )

        return cleaned_data