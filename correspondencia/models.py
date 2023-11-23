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
    remitente = models.CharField(max_length=300)
    
    codigo_hoja_ruta = models.CharField(null=True, blank=True)
    tipo_hoja_ruta = models.CharField(max_length=20)
    fecha_derivado = models.DateTimeField()
    asunto = models.CharField(max_length=300)


    

class Correspondencia(models.Model):
    numero_fojas = models.IntegerField()
    fecha_enviado = models.DateTimeField()
    fecha_recibido = models.DateTimeField(null=True, blank=True)
    fecha_devuelto = models.DateTimeField(null=True, blank=True)