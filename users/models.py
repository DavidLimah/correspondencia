from django.contrib.auth.models import AbstractUser
from django.db import models

# Módulo USERS
class CustomUser(AbstractUser):
    oficina = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)

