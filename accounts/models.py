from django.db import models
from django.contrib.auth.models import User

# 

class Oficina(models.Model):
	nombre_oficina = models.CharField(max_length=150)

	class Meta:
		verbose_name = 'Oficina'
		verbose_name_plurak = 'Oficina'

	def __str__(self):
		return self.nombre_oficina

class Cargo(models.Model):
	nombre_cargo = models.CharField(max_length=150)

	class Meta:
		verbose_name = 'Oficina'
		verbose_name_plurak = 'Oficina'
		
	def __str__(self):
		return self.nombre_cargo

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	image = models.ImageField(default='users/image_user.png',upload_to='users/')
	oficina = models.OneToOneField(Oficina, on_delete=models.CASCADE, related_name='oficina')
	cargo = models.OneToOneField(Cargo, on_delete=models.CASCADE, related_name='cargo')
