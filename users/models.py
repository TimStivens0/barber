from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    full_name = models.CharField('Full Name', max_length=200)
    phone = models.CharField('Phone', max_length=13, blank=True)
