from django import forms

from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["full_name", "username", "email", "password"]

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "input"}),
            "username": forms.TextInput(attrs={"class": "input"}),
            "email": forms.EmailInput(attrs={"class": "input"}),
            "password": forms.PasswordInput(attrs={"class": "input"}),
        }
