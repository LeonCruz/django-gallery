from django.shortcuts import render


# Create your views here.
def index(request, username):
    return render(request, "user_profile/index.html", {"user": username})
