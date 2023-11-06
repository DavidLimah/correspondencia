from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, relates_name = 'profile')
    oficina = models.OneToOneField(Oficina, verbose_name='Oficina')
    Cargo = models.OneToOneField(Cargo, verbose_name='Cargo')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    
