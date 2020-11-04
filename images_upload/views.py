from django import views
from django.shortcuts import redirect, render

from images_upload.forms import ImageUploadForm


# Create your views here.
def index(request):
    return render(request, "images_upload/index.html")


class ImageUploadView(views.View):
    template_name = "images_upload/index.html"
    form_class = ImageUploadForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()

            return redirect("profile:profile")

        return redirect(request.path)
