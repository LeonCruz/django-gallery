from django import forms
from django.contrib.auth.forms import AuthenticationForm

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

    def save(self):
        data = self.cleaned_data
        user = User(
            full_name=data["full_name"],
            username=data["username"],
            email=data["email"],
            password=data["password"],
        )
        user.set_password(data["password"])
        user.save()


class SignInForm(AuthenticationForm):
    pass
