from django.db import models



# Modelo Oficina
class Oficina(models.Model):
    nombre_oficina = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'oficina'
        verbose_name_plural = 'oficina'
    
    def __str__(self):
        return self.nombre_oficina


# Modelo Cargo
class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'cargo'
        verbose_name_plural = 'cargo'
    
    def __str__(self):
        return self.nombre_cargo

class Bandeja(models.Model):
    codigo_hoja_ruta = models.CharField(max_length=20, null=True, blank=True, default='S/C')
    usuario_remitente = models.CharField(max_length=200)
    oficina_remitente = models.CharField(max_length=200)
    cargo_remitente = models.CharField(max_length=200)
    numero_fojas = models.IntegerField()
    tipo_hoja_ruta = models.CharField(max_length=20)
    usuario_destino = models.CharField(max_length=200)
    oficina_destino = models.CharField(max_length=200)
    cargo_destino = models.CharField(max_length=200)
    correspondencia_derivada = models.BooleanField(default=False)
    correspondencia_devuelta = models.BooleanField(default=False)
    correspondencia_cancelada = models.BooleanField(default=False)
    correspondencia_recibido = models.BooleanField(default=False)
    correspondencia_devuelto = models.BooleanField(default=False)
    correspondencia_archivado = models.BooleanField(default=False)
    fecha_derivado = models.DateTimeField()
    fecha_recibido = models.DateTimeField(null=True, blank=True)
    fecha_devuelto = models.DateTimeField(null=True, blank=True)
    fecha_archivado = models.DateTimeField(null=True, blank=True)
    fecha_cancelado = models.DateTimeField(null=True, blank=True)
    asunto_hoja_ruta = models.CharField(max_length=300)
    observacion_devuelto = models.CharField(max_length=200, null=True, blank=True)
    observacion_cancelado = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'bandeja'
        verbose_name_plural = 'bandeja'
    
    def __str__(self):
        return self.usuario_remitente
    

