from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import SignupForm


# Create your views here.
@require_http_methods(["GET"])
def index(request):
    signup_form = SignupForm()
    return render(request, "accounts/index.html", {"form": signup_form})


@require_http_methods(["POST"])
def signup(request):
    signup_form = SignupForm(request.POST)

    if signup_form.is_valid():
        messages.success(request, "Cadastro realizado com sucesso")
        signup_form.save()
        return redirect("accounts:index")
    else:
        return redirect("accounts:index")
