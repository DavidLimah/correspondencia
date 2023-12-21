from django.forms import ModelForm
from accounts.models import Profile

from correspondencia.models import Correspondencia, Enviado, Oficina, Cargo

from django.contrib.auth.models import User

from django import forms

from django.contrib import messages


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    success_message = 'Exitoso'
    """

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


class DevueltoForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'


class CanceladoForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'

"""
class ArchivarForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = ['asunto_hoja_ruta']
        labels = {'asunto_hoja_ruta':'Asunto',}
"""
class ArchivarForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'
        #fields = ['asunto_archivado',]
