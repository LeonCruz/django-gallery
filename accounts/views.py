from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import SignInForm, SignupForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, "Cadastro realizado com sucesso.")
            return redirect("accounts:signin")

        return render(request, "accounts/index.html", {"form": signup_form})

    signup_form = SignupForm()
    return render(request, "accounts/index.html", {"form": signup_form})


@require_http_methods(["GET", "POST"])
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("profile:profile")

        messages.error(request, "Os dados fornecidos são inválidos")
        return redirect("accounts:signin")

    signin_form = SignInForm()
    return render(request, "accounts/signin.html", {"form": signin_form})


def signout(request):
    logout(request)
    return redirect("accounts:signin")
