from django.forms import ModelForm
from accounts.models import Profile

from correspondencia.models import Correspondencia, Unidad, TbConsejoMunicipal, TbDespachoAlcalde, TbSecretariaGeneral, TbSecAdmFinanciera, TbSecretariaTecnica, TbSecretariaPlanificacion, TbSecFortalecimientoInSocial, TbDirAsesoriaLegal, TbDireccionFinanzas, TbDirAuditoriaInterna, TbDirDesarrolloHumano, TbDireccionIngresos, TbDirDesProdMedAmbiente, TbDirUrbanismoCatastro, TbDirObrasPublicas, TbDireccionPlanificacion, TbDirSaneamientoBasico, TbDirAdministracionSalud, TbDirEduGestionSocial, TbAsesores, CrrConsejoMunicipal, CrrDespachoAlcalde, CrrSecretariaGeneral, CrrSecAdmFinanciera, CrrSecretariaTecnica, CrrSecretariaPlanificacion, CrrSecFortalecimientoInSocial, CrrDirAsesoriaLegal, CrrDireccionFinanzas, CrrDirAuditoriaInterna, CrrDirDesarrolloHumano, CrrDireccionIngresos, CrrDirDesProdMedAmbiente, CrrDirUrbanismoCatastro, CrrDirObrasPublicas, CrrDireccionPlanificacion, CrrDirSaneamientoBasico, CrrDirAdministracionSalud, CrrDirEduGestionSocial, CrrAsesores

from django.contrib.auth.models import User

from django import forms

from django.contrib import messages

"""
class SuccessMessageMixin:

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
"""

class CorrespondenciaForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = ["usuario_rtte","unidad_rtte","cargo_rtte","asunto_derivado","usuario_destino","unidad_destino","cargo_destino","tipo_derivado","numero_fojas","archivo",]


class EnviadoForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = '__all__'


# Archivar
class ArchivarForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = ["usuario_rtte","unidad_rtte","cargo_rtte","asunto_archivado",]
        labels = {"usuario_rtte":"Usuario remitente","unidad_rtte":"Unidad","cargo_rtte":"Cargo","asunto_archivado":"Asunto archivado",}


# Devolver
class DevolverForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = ["usuario_rtte","unidad_rtte","cargo_rtte","asunto_devuelto",]
        labels = {"usuario_rtte":"Usuario remitente","unidad_rtte":"Unidad","cargo_rtte":"Cargo","asunto_devuelto":"Asunto devuelto",}


# Cancelar
class CancelarForm(ModelForm):
    class Meta:
        model = Correspondencia
        fields = ["usuario_rtte","unidad_rtte","cargo_rtte","asunto_cancelado",]
        labels = {"usuario_rtte":"Usuario remitente","unidad_rtte":"Unidad","cargo_rtte":"Cargo","asunto_cancelado":"Asunto cancelado",}

# Correspondencia Consejo Municipal
class CrrConsejoMunicipalForm(ModelForm):
    class Meta:
        model = CrrConsejoMunicipal
        fields = '__all__'

# Correspondencia Despacho Alcalde
class CrrDespachoAlcaldeForm(ModelForm):
    class Meta:
        model = CrrDespachoAlcalde
        fields = '__all__'

# Correspondencia Secretaria General
class CrrSecretariaGeneralForm(ModelForm):
    class Meta:
        model = CrrSecretariaGeneral
        fields = '__all__'


# Correspondencia Administración Financiera
class CrrSecAdmFinancieraForm(ModelForm):
    class Meta:
        model = CrrSecAdmFinanciera
        fields = '__all__'


# Correspondencia Secretaria Técnica
class CrrSecretariaTecnicaForm(ModelForm):
    class Meta:
        model = CrrSecretariaTecnica
        fields = '__all__'


# Correspondencia Secretaría Planificación
class CrrSecretariaPlanificacionForm(ModelForm):
    class Meta:
        model = CrrSecretariaPlanificacion
        fields = '__all__'


# Correspondencia Secretaría Fortalecimiento Institucional Social
class CrrSecFortalecimientoInSocialForm(ModelForm):
    class Meta:
        model = CrrSecFortalecimientoInSocial
        fields = '__all__'


# Correspondencia Asesoria Legal
class CrrDirAsesoriaLegalForm(ModelForm):
    class Meta:
        model = CrrDirAsesoriaLegal
        fields = '__all__'


# Correspondencia Dirección Finanzas
class CrrDireccionFinanzasForm(ModelForm):
    class Meta:
        model = CrrDireccionFinanzas
        fields = '__all__'


# Correspondencia Auditoria Interna
class CrrDirAuditoriaInternaForm(ModelForm):
    class Meta:
        model = CrrDirAuditoriaInterna
        fields = '__all__'


# Correspondencia Dirección Desarrollo Humano
class CrrDirDesarrolloHumanoForm(ModelForm):
    class Model:
        model = CrrDirDesarrolloHumano
        fields = '__all__'


# Correspondencia Cirección Ingresos
class CrrDireccionIngresosForm(ModelForm):
    class Meta:
        model = CrrDireccionIngresos
        fields = '__all__'


# Correspondencia Dirección Productiva y Medio Ambiente
class CrrDirDesProdMedAmbienteForm(ModelForm):
    class Meta:
        model = CrrDirDesProdMedAmbiente
        fields = '__all__'


# Correspondencia Dirección Urbanismo y Catastro
class CrrDirUrbanismoCatastroForm(ModelForm):
    class Meta:
        model = CrrDirUrbanismoCatastro
        fields = '__all__'


# Correspondencia Dirección Obras Públicas
class CrrDirObrasPublicasForm(ModelForm):
    class Meta:
        model = CrrDirObrasPublicas
        fields = '__all__'


# Correspondencia Dirección Planificación
class CrrDireccionPlanificacionForm(ModelForm):
    class Meta:
        model = CrrDireccionPlanificacion
        fields = '__all__'


# Correspondencia Dirección Saneamiento Básico
class CrrDirSaneamientoBasicoForm(ModelForm):
    class Meta:
        model = CrrDirSaneamientoBasico
        fields = '__all__'


# Correspondencia Dirección Administración Salud
class CrrDirAdministracionSaludForm(ModelForm):
    class Meta:
        model = CrrDirAdministracionSalud
        fields = '__all__'


# Correspondencia Dirección Educación Gestión Social
class CrrDirEduGestionSocialForm(ModelForm):
    class Meta:
        model = CrrDirEduGestionSocial
        fields = '__all__'


# Correspondencia Asesores
class CrrAsesoresForm(ModelForm):
    class Meta:
        model = CrrAsesores
        fields = '__all__'
