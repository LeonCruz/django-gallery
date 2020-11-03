from accounts.models import User
from django.db import models


# Create your models here.
class Images(models.Model):
    image_path = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
