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
class TbConsejoMunicipal(models.Model):
    nombre_cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'consejo municipal'
        verbose_name_plural = 'consejo municipal'

    def __str__(self):
        return "Consejo Municipal"

    def get_absolute_url(self):
        return reverse('consejo municipal', kwargs={'pk': self.pk})


# Unidad DEspacho Alcalde
class TbDespachoAlcalde(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'despacho alcalde'
        verbose_name_plural = 'despacho alcalde'

    def __str__(self):
        return "Despacho Alcalde"

    def get_absolute_url(self):
        return reverse('despacho-alcalde', kwargs={'pk': self.pk})


# Unidad Secretaría general
class TbSecretariaGeneral(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'secretaria general'
        verbose_name_plural = 'secretaria general'

    def __str__(self):
        return "Secretaria General"

    def get_absolute_url(self):
        return reverse('secretaria-general', kwargs={'pk': self.pk})


# Unidad Secretaría Administrativa Financiera
class TbSecAdmFinanciera(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'administracion financiera'
        verbose_name_plural = 'administracion financiera'

    def __str__(self):
        return "Secretaria Administrativa Financiera"

    def get_absolute_url(self):
        return reverse('administracion-financiera', kwargs={'pk': self.pk})


# Secretaría Técnica
class TbSecretariaTecnica(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'secretaria tecnica'
        verbose_name_plural = 'secretaria tecnica'

    def __str__(self):
        return "Secretaria Tecnica"

    def get_absolute_url(self):
        return reverse('secretaria-tecnica', kwargs={'pk': self.pk})


# Secretaría Planificación
class TbSecretariaPlanificacion(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'planificacion'
        verbose_name_plural = 'planificacion'

    def __str__(self):
        return "Secretaria Planificacion"

    def get_absolute_url(self):
        return reverse('planificacion', kwargs={'pk': self.pk})


# Unidad Secretaría Fortalecimiento Institucional Social
class TbSecFortalecimientoInSocial(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'fortalecimiento social'
        verbose_name_plural = 'fortalecimiento social'

    def __str__(self):
        return "Secretaria Fortalecimiento Institucional Social"

    def get_absolute_url(self):
        return reverse('fortalecimiento-social', kwargs={'pk': self.pk})


# Unidad Asesoria Legal
class TbDirAsesoriaLegal(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'asesoria legal'
        verbose_name_plural = 'asesoria legal'

    def __str__(self):
        return "Direccion Asesoria Legal"

    def get_absolute_url(self):
        return reverse('asesoria-legal', kwargs={'pk': self.pk})


# Unidad Direccion Finanzas
class TbDireccionFinanzas(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'asesoria legal'
        verbose_name_plural = 'asesoria legal'

    def __str__(self):
        return "Direccion Finanzas"

    def get_absolute_url(self):
        return reverse('direccion-finanzas', kwargs={'pk': self.pk})


# Unidad Direccion de Finanzas
class TbDirAuditoriaInterna(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'auditoria financiera'
        verbose_name_plural = 'auditoria financiera'

    def __str__(self):
        return "Direccion Auditoria Interna"

    def get_absolute_url(self):
        return reverse('auditoria-financiera', kwargs={'pk': self.pk})


# Unidad Direccion Auditoria Interna
class TbDirDesarrolloHumano(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'desarrollo humano'
        verbose_name_plural = 'desarrollo humano'

    def __str__(self):
        return "Direccion de Desarrollo Humano"

    def get_absolute_url(self):
        return reverse('desarrollo-humano', kwargs={'pk': self.pk})


# Unidad Dirección Ingresos
class TbDireccionIngresos(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'direccion ingresos'
        verbose_name_plural = 'direccion ingresos'

    def __str__(self):
        return "Direccion de Ingresos"

    def get_absolute_url(self):
        return reverse('direccion-ingresos', kwargs={'pk': self.pk})


# Unidad Dirección de Desarrollo Productivo y Medio Ambiente
class TbDirDesProdMedAmbiente(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'desarollo productivo'
        verbose_name_plural = 'desarollo productivo'

    def __str__(self):
        return "Direccion de Desarrollo Productivo y Medio Ambiente"

    def get_absolute_url(self):
        return reverse('desarollo-productivo', kwargs={'pk': self.pk})


# Unidad Dirección Urbanismo y Catastro
class TbDirUrbanismoCatastro(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'urbanismo catastro'
        verbose_name_plural = 'urbanismo catastro'

    def __str__(self):
        return "Direccion Urbanismo y Catastro"

    def get_absolute_url(self):
        return reverse('urbanismo-catastro', kwargs={'pk': self.pk})


# Dirección Obras Públicas
class TbDirObrasPublicas(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'obras publicas'
        verbose_name_plural = 'obras publicas'

    def __str__(self):
        return "Direccion Obras Publicas"

    def get_absolute_url(self):
        return reverse('obras-publicas', kwargs={'pk': self.pk})


# Unidad Dirección Planificación
class TbDireccionPlanificacion(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'planificacion'
        verbose_name_plural = 'planificacion'

    def __str__(self):
        return "Direccion de Planificacion"

    def get_absolute_url(self):
        return reverse('planificacion', kwargs={'pk': self.pk})


# Unidad Dirección Saneamiento Básico
class TbDirSaneamientoBasico(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'saneamiento basico'
        verbose_name_plural = 'saneamiento basico'

    def __str__(self):
        return "Direccion Saneamiento Basico"

    def get_absolute_url(self):
        return reverse('saneamiento-basico', kwargs={'pk': self.pk})


# Unidad Dirección Administración Salud
class TbDirAdministracionSalud(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'administracion salud'
        verbose_name_plural = 'administracion salud'

    def __str__(self):
        return "Direccion Administracion Salud"

    def get_absolute_url(self):
        return reverse('administracion-salud', kwargs={'pk': self.pk})


# Direccion de Educación y Gestión Social
class TbDirEduGestionSocial(models.Model):
    nombre_cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'administracion salud'
        verbose_name_plural = 'administracion salud'

    def __str__(self):
        return "Direccion de Educacion y Gestion Social"

    def get_absolute_url(self):
        return reverse('administracion-salud', kwargs={'pk': self.pk})


# Unidad Asesores
class TbAsesores(models.Model):
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
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_crr')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_crr')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_crr')
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
class CrrConsejoMunicipal(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_cm')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_cm')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_cm')
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


# Modelo despacho alcalde
class CrrDespachoAlcalde(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_da')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_da')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_da')
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


# Modelo Secretaria Municipal General
class CrrSecretariaGeneral(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_sg')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_sg')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_sg')
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


# Modelo Secretaría Administrativa financiera
class CrrSecAdmFinanciera(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_saf')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_saf')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_saf')
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


# Modelo Secretaría Municipal Técnico
class CrrSecretariaTecnica(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_st')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_st')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_st')
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


# Modelo Secretaría Planificación
class CrrSecretariaPlanificacion(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_sp')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_sp')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_sp')
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


# Modelo Secretaría Municipal de Fortalecimiento Institucional
class CrrSecFortalecimientoInSocial(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_sfis')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_sfis')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_sfis')
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

# Modelo Dirección de Asesoría legal
class CrrDirAsesoriaLegal(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_dal')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_dal')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_dal')
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


# Modelo Dirección de Finanzas
class CrrDireccionFinanzas(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_df')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_df')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_df')
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


# Modelo Dirección de Auditoría Interna
class CrrDirAuditoriaInterna(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_dai')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_dai')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_dai')
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


# Modelo Dirección de Desarrollo Humano
class CrrDirDesarrolloHumano(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_ddh')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_ddh')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_ddh')
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


# Modelo ´Dirección de Ingresos
class CrrDireccionIngresos(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_di')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_di')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_di')
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


# Modelo Dirección de Desarrollo Productivo y Medio Ambiente
class CrrDirDesProdMedAmbiente(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_ddpma')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_ddpma')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_ddpma')
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


# Modelo Dirección de Urbanismo y Catastro
class CrrDirUrbanismoCatastro(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_duc')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_duc')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_duc')
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


# Modelo Dirección de Obras Públicas
class CrrDirObrasPublicas(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_dop')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_dop')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_dop')
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


# Modelo Dirección de Planificación
class CrrDireccionPlanificacion(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_dpl')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_dpl')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_dpl')
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


# Modelo Dirección de Saneamiento Básico
class CrrDirSaneamientoBasico(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_dsb')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_dsb')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_dsb')
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


# Modelo Dirección de Administración de Salud
class CrrDirAdministracionSalud(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_das')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_das')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_das')
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


# Modelo Dirección de Educación y Gestión Social
class CrrDirEduGestionSocial(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_degs')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_degs')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_degs')
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


# Modelo Asesores
class CrrAsesores(models.Model):
    nombre_unidad = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, default='S/C', null=True, blank=True)
    usuario_rtte = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_rtte_as')
    numero_fojas = models.IntegerField(null=True, blank=True)
    tipo_derivado = models.CharField(choices=options_tipo,max_length=200)
    unidad_destino = models.ForeignKey(Unidad, on_delete=models.CASCADE, related_name='unidad_destino_as')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino_as')
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