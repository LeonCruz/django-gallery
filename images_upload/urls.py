from django.urls import path

from images_upload import views

app_name = "upload"
urlpatterns = [path("", views.index, name="index")]
