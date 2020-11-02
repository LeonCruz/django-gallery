from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url="accounts:signin")
def index(request):
    return render(request, "user_profile/index.html")
