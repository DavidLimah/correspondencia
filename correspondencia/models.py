from django.db import models

from django.contrib.auth.models import User
#from accounts.models import Profile




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
    ['INFORME', 'Informe'],
    ['NOTA_INTERNA', 'Nota interna'],
    ['NOTA_EXTERNA', 'Nota externa']
]

usuario_rtte_opts = User.objects.all()
usuario_destino_opts = User.objects.all()

class Correspondencia(models.Model):
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte')
    #nombre_rtte = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='nombre_rtte')
    #oficina_rtte = models.OneToOneField(Oficina, on_delete=models.CASCADE, related_name='oficina')
    #cargo_rtte = models.OneToOneField(Cargo, on_delete=models.CASCADE, related_name='cargo')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_hoja_ruta = models.CharField(choices=options_tipo,max_length=200)
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino')
    #nombre_destino = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='usuario_destino')
    #oficina_destino = models.OneToOneField(Oficina, on_delete=models.CASCADE, related_name='oficina')
    #cargo_destino = models.OneToOneField(Cargo, on_delete=models.CASCADE, related_name='cargo')
    derivado = models.BooleanField(default=True, null=True, blank=True)
    recibido = models.BooleanField(default=True, null=True, blank=True)
    devuelto = models.BooleanField(default=False, null=True, blank=True)
    cancelado = models.BooleanField(default=False, null=True, blank=True)
    archivado = models.BooleanField(default=False, null=True, blank=True)
    pendiente = models.BooleanField(default=False, null=True, blank=True)
    fecha_derivado = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_recibido = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_devuelto = models.DateTimeField(null=True, blank=True)
    fecha_cancelado = models.DateTimeField(null=True, blank=True)
    fecha_archivado = models.DateTimeField(null=True, blank=True)
    asunto_hoja_ruta = models.CharField(max_length=300, null=True, blank=True)
    asunto_devuelto = models.CharField(max_length=200, null=True, blank=True)
    asunto_cancelado = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'correspondencia'
        verbose_name_plural = 'correspondencias'
    
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
    

