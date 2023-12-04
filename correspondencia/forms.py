from django.forms import ModelForm
from accounts.models import Profile
from correspondencia.models import Bandeja, Enviado


from django.contrib import messages


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = 'Exitoso'

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data




class BandejaForm(ModelForm):
	class Meta:
		model = Bandeja
		# fields = ['usuario_remitente','oficina_remitente','cargo_remitente','numero_fojas','tipo_hoja_ruta','usuario_destino','oficina_destino','cargo_destino','fecha_derivado','asunto_hoja_ruta']
		fields = '__all__'
class EnviadoForm(ModelForm):
    class Meta:
        model = Enviado
        fields = ['user_remitente','of_remitente','car_remitente','user_destinatario','asunto_hr','num_fojas',]
        labels = {"user_remitente":"Remitente","of_remitente":"Oficina","car_remitente":"Cargo","user_destinatario":"Destinatario","asunto_hr":"Asunto","num_fojas":"Numero fojas",}


"""
# CODIGO QUE FUNCIONA
class EnviadoForm(ModelForm):
    class Meta:
        model = Enviado
        fields = '__all__'

from django.shortcuts import render
from .models import MyModel
from .forms import MyForm

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})



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