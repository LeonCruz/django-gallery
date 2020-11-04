from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url="accounts:signin")
def index(request):
    images = request.user.images_set.order_by("-uploaded_at")
    return render(request, "user_profile/index.html", {"images": images})
