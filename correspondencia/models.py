from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

#from accounts.models import Profile


options_tipo = [
    ['INFORME', 'Informe'],
    ['NOTA_INTERNA', 'Nota interna'],
    ['NOTA_EXTERNA', 'Nota externa']
]


# Modelo Unidades
class Unidad(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    sigla_unidad = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'unidad'
        verbose_name_plural = 'unidades'

    def __str__(self):
        return self.nombre_unidad

    def get_absolute_url(self):
        return reverse('unidad', kwargs={'pk': self.pk})


# Modelo Correspondencia
class Correspondencia(models.Model):
    nombre_unidad = models.CharField(max_length=200, default='UNIDAD 1')
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_hoja_ruta = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino')
    derivado = models.BooleanField(default=True, null=True, blank=True)
    recibido = models.BooleanField(default=True, null=True, blank=True)
    devuelto = models.BooleanField(default=False, null=True, blank=True)
    cancelado = models.BooleanField(default=False, null=True, blank=True)
    archivado = models.BooleanField(default=False, null=True, blank=True)
    fecha_derivado = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_recibido = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_devuelto = models.DateTimeField(null=True, blank=True)
    fecha_cancelado = models.DateTimeField(null=True, blank=True)
    fecha_archivado = models.DateTimeField(null=True, blank=True)
    asunto_hoja_ruta = models.CharField(max_length=300, null=True, blank=True)
    asunto_devuelto = models.CharField(max_length=200, null=True, blank=True)
    asunto_archivado = models.CharField(max_length=200, null=True, blank=True)
    asunto_cancelado = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'correspondencia'
        verbose_name_plural = 'correspondencias'

    def __str__(self):
        return self.usuario_remitente

    def get_absolute_url(self):
        return reverse('codigo', kwargs={'pk': self.pk})


# Modelo Concejo Municipal 
class consejo_municipal(models.Model):
    pass


# Modelo despacho alcalde
class despacho_alcalde(models.Model):
    pass


# Modelo Secretaria Municipal General
class sm_general(models.Model):
    pass


# Modelo Secretaría Administrativa financiera
class sm_adm_financiero(models.Model):
    pass


# Modelo Secretaría Municipal Técnico
class sm_tecnico(models.Model):
    pass


# Modelo Secretaría Planificación
class sm_planificacion(models.Model):
    pass


# Modelo Secretaría Municipal de Fortalecimiento Institucional
class sm_fortalecimiento_ins_social(models.Model):
    pass

# Modelo Dirección de Asesoría legal
class dir_asesoria_legal(models.Model):
    pass


# Modelo Dirección de Finanzas
class dir_finanzas(models.Model):
    pass


# Modelo Dirección de Auditoría Interna
class dir_auditoria_interna(models.Model):
    pass


# Modelo Dirección de Desarrollo Humano
class dir_desarrollo_humano(models.Model):
    pass


# Modelo ´Dirección de Ingresos
class dir_ingresos(models.Model):
    pass


# Modelo Dirección de Desarrollo Productivo y Medio Ambiente
class dir_des_prod_medio_ambiente(models.Model):
    pass


# Modelo Dirección de Urbanismo y Catastro
class dir_urbanismo_catastro(models.Model):
    pass


# Modelo Dirección de Obras Públicas
class dir_obras_publicas(models.Model):
    pass


# Modelo Dirección de Planificación
class dir_planificacion(models.Model):
    pass


# Modelo Dirección de Saneamiento Básico
class dir_saneamiento_basico(models.Model):
    pass


# Modelo Dirección de Administración de Salud
class dir_adm_salud(models.Model):
    pass


# Modelo Dirección de Educación y Gestión Social
class dir_edu_gestion_social(models.Model):
    pass


# Modelo Asesores
class asesores(models.Model):
    pass