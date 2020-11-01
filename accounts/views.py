from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import SignupForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, "Cadastro realizado com sucesso.")
            return redirect("accounts:index")

        return render(request, "accounts/index.html", {"form": signup_form})

    signup_form = SignupForm()
    return render(request, "accounts/index.html", {"form": signup_form})
