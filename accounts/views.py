from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import SignupForm


# Create your views here.
@require_http_methods(["GET"])
def index(request):
    signup_form = SignupForm()
    return render(request, "accounts/index.html", {"form": signup_form})
