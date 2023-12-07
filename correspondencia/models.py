from django.db import models

from django.contrib.auth.models import User



# Modelo Oficina
class Oficina(models.Model):
    nombre_oficina = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'oficina'
        verbose_name_plural = 'oficinas'
    
    def __str__(self):
        return self.nombre_oficina


# Modelo Cargo
class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'
    
    def __str__(self):
        return self.nombre_cargo

options_tipo = [
    [0, 'Informe'],
    [1, 'Nota interna'],
    [2, 'Nota externa']
]

class Bandeja(models.Model):
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.CharField(max_length=20, null=True, blank=True)
    nombre_rtte = models.CharField(max_length=200, null=True, blank=True)
    oficina_rtte = models.CharField(max_length=200, null=True, blank=True)
    cargo_rtte = models.CharField(max_length=200, null=True, blank=True)
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_hoja_ruta = models.IntegerField(choices=options_tipo)
    usuario_destino = models.CharField(max_length=200, null=True, blank=True)
    nombre_destino = models.CharField(max_length=200, null=True, blank=True)
    oficina_destino = models.CharField(max_length=200, null=True, blank=True)
    cargo_destino = models.CharField(max_length=200, null=True, blank=True)
    derivado = models.BooleanField(default=False, null=True, blank=True)
    recibido = models.BooleanField(default=False, null=True, blank=True)
    devuelto = models.BooleanField(default=False, null=True, blank=True)
    cancelado = models.BooleanField(default=False, null=True, blank=True)
    archivado = models.BooleanField(default=False, null=True, blank=True)
    pendiente = models.BooleanField(default=False, null=True, blank=True)
    fecha_derivado = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_recibido = models.DateTimeField(null=True, blank=True)
    fecha_devuelto = models.DateTimeField(null=True, blank=True)
    fecha_cancelado = models.DateTimeField(null=True, blank=True)
    fecha_archivado = models.DateTimeField(null=True, blank=True)
    asunto_hoja_ruta = models.CharField(max_length=300, null=True, blank=True)
    asunto_devuelto = models.CharField(max_length=200, null=True, blank=True)
    asunto_cancelado = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'bandeja'
        verbose_name_plural = 'bandeja'
    
    def __str__(self):
        return self.usuario_remitente


class Enviado(models.Model):
    user_remitente = models.CharField(max_length=200, null=True, blank=True)
    of_remitente = models.CharField(max_length=200, null=True, blank=True)
    car_remitente = models.CharField(max_length=200, null=True, blank=True)
    user_destinatario = models.CharField(max_length=200, null=True, blank=True)
    asunto_hr = models.CharField(max_length=200, null=True, blank=True)
    num_fojas = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        verbose_name = 'enviado'
        verbose_name_plural = 'enviados'
    
    def __str__(self):
        return self.user_remitente
    

