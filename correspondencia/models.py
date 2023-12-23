from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

#from accounts.models import Profile


options_tipo = [
    ['INFORME', 'Informe'],
    ['NOTA_INTERNA', 'Nota interna'],
    ['NOTA_EXTERNA', 'Nota externa']
]


# Unidades
class Unidad(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    sigla_unidad = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'unidad'
        verbose_name_plural = 'unidad'

    def __str__(self):
        return self.nombre_unidad

    def get_absolute_url(self):
        return reverse('Unidad', kwargs={'pk': self.pk})


# Unidad Consejo Municipal
class ConsejoMunicipal(models.Model):
    sigla_unidad = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'consejo municipal'
        verbose_name_plural = 'consejo municipal'

    def __str__(self):
        return "Consejo Municipal"

    def get_absolute_url(self):
        return reverse('consejo municipal', kwargs={'pk': self.pk})


# Unidad DEspacho Alcalde
class DespachoAlcalde(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'despacho alcalde'
        verbose_name_plural = 'despacho alcalde'

    def __str__(self):
        return "Despacho Alcalde"

    def get_absolute_url(self):
        return reverse('despacho-alcalde', kwargs={'pk': self.pk})


# Unidad Secretaría general
class SecretariaGeneral(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'secretaria general'
        verbose_name_plural = 'secretaria general'

    def __str__(self):
        return "Secretaria General"

    def get_absolute_url(self):
        return reverse('secretaria-general', kwargs={'pk': self.pk})


# Unidad Secretaría Administrativa Financiera
class SecAdmFinanciera(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'administracion financiera'
        verbose_name_plural = 'administracion financiera'

    def __str__(self):
        return "Secretaria Administrativa Financiera"

    def get_absolute_url(self):
        return reverse('administracion-financiera', kwargs={'pk': self.pk})


# Secretaría Técnica
class SecretariaTecnica(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'secretaria tecnica'
        verbose_name_plural = 'secretaria tecnica'

    def __str__(self):
        return "Secretaria Tecnica"

    def get_absolute_url(self):
        return reverse('secretaria-tecnica', kwargs={'pk': self.pk})


# Secretaría Planificación
class SecretariaPlanificacion(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'planificacion'
        verbose_name_plural = 'planificacion'

    def __str__(self):
        return "Secretaria Planificacion"

    def get_absolute_url(self):
        return reverse('planificacion', kwargs={'pk': self.pk})


# Unidad Secretaría Fortalecimiento Institucional Social
class SecFortalecimientoInSocial(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'fortalecimiento social'
        verbose_name_plural = 'fortalecimiento social'

    def __str__(self):
        return "Secretaria Fortalecimiento Institucional Social"

    def get_absolute_url(self):
        return reverse('fortalecimiento-social', kwargs={'pk': self.pk})


# Unidad Asesoria Legal
class DirAsesoriaLegal(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'asesoria legal'
        verbose_name_plural = 'asesoria legal'

    def __str__(self):
        return "Direccion Asesoria Legal"

    def get_absolute_url(self):
        return reverse('asesoria-legal', kwargs={'pk': self.pk})


# Unidad Direccion Finanzas
class DireccionFinanzas(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'asesoria legal'
        verbose_name_plural = 'asesoria legal'

    def __str__(self):
        return "Direccion Finanzas"

    def get_absolute_url(self):
        return reverse('direccion-finanzas', kwargs={'pk': self.pk})


# Unidad Direccion de Finanzas
class DirAuditoriaInterna(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'auditoria financiera'
        verbose_name_plural = 'auditoria financiera'

    def __str__(self):
        return "Direccion Auditoria Interna"

    def get_absolute_url(self):
        return reverse('auditoria-financiera', kwargs={'pk': self.pk})


# Unidad Direccion Auditoria Interna
class DirDesarrolloHumano(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'desarrollo humano'
        verbose_name_plural = 'desarrollo humano'

    def __str__(self):
        return "Direccion de Desarrollo Humano"

    def get_absolute_url(self):
        return reverse('desarrollo-humano', kwargs={'pk': self.pk})


# Unidad Dirección Ingresos
class DireccionIngresos(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'direccion ingresos'
        verbose_name_plural = 'direccion ingresos'

    def __str__(self):
        return "Direccion de Ingresos"

    def get_absolute_url(self):
        return reverse('direccion-ingresos', kwargs={'pk': self.pk})


# Unidad Dirección de Desarrollo Productivo y Medio Ambiente
class DirDesProdMedAmbiente(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'desarollo productivo'
        verbose_name_plural = 'desarollo productivo'

    def __str__(self):
        return "Direccion de Desarrollo Productivo y Medio Ambiente"

    def get_absolute_url(self):
        return reverse('desarollo-productivo', kwargs={'pk': self.pk})


# Unidad Dirección Urbanismo y Catastro
class DirUrbanismoCatastro(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'urbanismo catastro'
        verbose_name_plural = 'urbanismo catastro'

    def __str__(self):
        return "Direccion Urbanismo y Catastro"

    def get_absolute_url(self):
        return reverse('urbanismo-catastro', kwargs={'pk': self.pk})


# Dirección Obras Públicas
class DirObrasPublicas(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'obras publicas'
        verbose_name_plural = 'obras publicas'

    def __str__(self):
        return "Direccion Obras Publicas"

    def get_absolute_url(self):
        return reverse('obras-publicas', kwargs={'pk': self.pk})


# Unidad Dirección Planificación
class DireccionPlanificacion(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'planificacion'
        verbose_name_plural = 'planificacion'

    def __str__(self):
        return "Direccion de Planificacion"

    def get_absolute_url(self):
        return reverse('planificacion', kwargs={'pk': self.pk})


# Unidad Dirección Saneamiento Básico
class DirSaneamientoBasico(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'saneamiento basico'
        verbose_name_plural = 'saneamiento basico'

    def __str__(self):
        return "Direccion Saneamiento Basico"

    def get_absolute_url(self):
        return reverse('saneamiento-basico', kwargs={'pk': self.pk})


# Unidad Dirección Administración Salud
class DirAdministracionSalud(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'administracion salud'
        verbose_name_plural = 'administracion salud'

    def __str__(self):
        return "Direccion Administracion Salud"

    def get_absolute_url(self):
        return reverse('administracion-salud', kwargs={'pk': self.pk})


# Direccion de Educación y Gestión Social
class DirEduGestionSocial(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'administracion salud'
        verbose_name_plural = 'administracion salud'

    def __str__(self):
        return "Direccion de Educacion y Gestion Social"

    def get_absolute_url(self):
        return reverse('administracion-salud', kwargs={'pk': self.pk})


# Unidad Asesores
class AsesoresU(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'asesor'
        verbose_name_plural = 'asesor'

    def __str__(self):
        return "Asesores"

    def get_absolute_url(self):
        return reverse('asesores', kwargs={'pk': self.pk})


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
    asunto_derivado = models.CharField(max_length=300, null=True, blank=True)
    asunto_devuelto = models.CharField(max_length=200, null=True, blank=True)
    asunto_archivado = models.CharField(max_length=200, null=True, blank=True)
    asunto_cancelado = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'correspondencia'
        verbose_name_plural = 'correspondencia'

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
class AsesoresC(models.Model):
    pass