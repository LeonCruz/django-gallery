from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "input"}),
            "email": forms.TextInput(attrs={"class": "input"}),
            "password": forms.PasswordInput(attrs={"class": "input"}),
        }
