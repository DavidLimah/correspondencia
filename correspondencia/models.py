from django.db import models

# Modelo Oficina
class Oficina(models.Model):
    nombre_oficina = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'oficina'
        verbose_name_plural = 'oficina'
    
    def __str__(self):
        return self.nombre_oficina


# Modelo Cargo
class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'cargo'
        verbose_name_plural = 'cargo'
    
    def __str__(self):
        return self.nombre_cargo

class Derivacion(models.Model):
    pass

class Correspondencia(models.Model):
    pass