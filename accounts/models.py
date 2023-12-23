from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from correspondencia.models import Oficina, Cargo
 

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	image = models.ImageField(default='users/image_user.png',upload_to='users/')
	# oficina = models.ForeignKey(Oficina, related_name='oficina', on_delete=models.CASCADE, null=True, blank=True)
	# cargo = models.ForeignKey(Cargo, related_name='cargo', on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfiles'
		ordering = ['id']

	def __str__(self):
		return f'{self.user} {self.oficina} {self.cargo}'

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
