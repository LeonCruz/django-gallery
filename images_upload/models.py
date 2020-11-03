from accounts.models import User
from django.db import models


def path_file(instance, filename):
    return f"uploads/{instance.user.id}/{filename}"


# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to=path_file)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
