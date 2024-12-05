from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    name_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    x_coord = models.TextField()
    y_coord = models.TextField()