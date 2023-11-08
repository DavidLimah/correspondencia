from django.db import models

# from django.contrib.auth.models import User

from app_correspondencia.models import CustomUser

from django.db.models.signals import post_save

from django.dispatch import receiver

class Oficina(models.Model):
    nombre_oficina = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
    
    def __str__(self):
        return nombre_oficina

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
    
    def __str__(self):
        return nombre_cargo


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name = 'profile')
    oficina = models.OneToOneField(Oficina, verbose_name='Oficina', on_delete = models.CASCADE)
    Cargo = models.OneToOneField(Cargo, verbose_name='Cargo', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(save_user_profile, sender=CustomUser)