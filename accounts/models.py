from django.db import models
from django.contrib.auth.models import User

# 

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	image = models.ImageField(default='users/image_user.png',upload_to='users/')
	location = models.CharField(max_length=80, null=True, blank=True)
