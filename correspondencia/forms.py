from django.forms import ModelForm
from accounts.models import Profile
from correspondencia.models import Bandeja, Enviado


class BandejaForm(ModelForm):
	class Meta:
		model = Bandeja
		# fields = ['usuario_remitente','oficina_remitente','cargo_remitente','numero_fojas','tipo_hoja_ruta','usuario_destino','oficina_destino','cargo_destino','fecha_derivado','asunto_hoja_ruta']
		fields = '__all__'


class EnviadoForm(ModelForm):
    class Meta:
        model = Enviado
        fields = '__all__'


"""

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

"""