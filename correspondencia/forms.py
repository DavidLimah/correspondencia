from django.forms import ModelForm
from accounts.models import Profile

from correspondencia.models import Correspondencia

from django.contrib.auth.models import User

from django import forms

from django.contrib import messages


class SuccessMessageMixin:

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class CorrespondenciaForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = ['codigo', 'usuario_rtte', 'numero_fojas', 'tipo_hoja_ruta', 'usuario_destino', 'asunto_hoja_ruta', ]


class EnviadoForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'


# Acciones

# Archivar
class ArchivarForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'


# Devolver
class DevolverForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'


# Cancelar
class CancelarForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'

