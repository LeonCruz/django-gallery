from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url="accounts:signin")
def index(request):
    lista = list(range(1, 11))
    return render(request, "user_profile/index.html", {"lista": lista})
