from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    university = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=9)
