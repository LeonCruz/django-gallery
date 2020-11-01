from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    path("", views.signup, name="index"),
    path("signup/", views.signup, name="signup"),
]
