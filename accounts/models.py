from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.CharField(unique=True, max_length=150)
    full_name = models.CharField(max_length=100, null=False, blank=False)
