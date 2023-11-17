from django.db import models

# from simple_history.models import HistoricalRecords

# Modelo GESTION
class Gestion(models.Model):
	codigo = models.CharField(max_length=4)
	descripcion = models.CharField(max_length=20)
	estado = models.IntegerField()
	numero = models.IntegerField()

	class Meta:
		verbose_name = 'Gestion'
		verbose_name_plural = 'Gestiones'
	
	def __str__(self):
		return self.codigo



# Modelo PROFESIONES
class Profesiones(models.Model):
	nombre_profesion = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Profesion'
		verbose_name_plural = 'Profesiones'
	
	def __str__(self):
		return self.nombre_profesion

# Modelo OFICINA
class Oficina(models.Model):
	nombre_oficina = models.CharField(max_length=200)
	# history = HistoricalRecords()

	class Meta:
		verbose_name = 'oficina'
		verbose_name_plural = 'oficinas'
	
	def __str__(self):
		return self.nombre_oficina

# Modelo USUARIOS
class Usuarios(models.Model):
	nombres = models.CharField(max_length=80)
	paterno = models.CharField(max_length=50)
	materno = models.CharField(max_length=50)
	fecha_nacimiento = models.DateTimeField()
	fk_profesion = models.ForeignKey(Profesiones, related_name='fk_profesion', on_delete=models.CASCADE)
	estado = models.IntegerField()
	ci = models.CharField(max_length=20)

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
	
	def __str__(self):
		return self.nombre


# Modelo USUARIO OFICINA
class UsuarioOficina(models.Model):
	fk_usuario = models.ForeignKey(Usuarios, related_name='fk_usuario', on_delete=models.CASCADE)
	fk_oficina = models.ForeignKey(Oficina, related_name='fk_oficina',on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField()
	responsable = models.BooleanField()
	activo = models.BooleanField()
	
	class Meta:
		verbose_name = 'Usuario oficina'
		verbose_name_plural = 'Usuario Oficina'
	
	def __str__(self):
		return self.fk_usuario

# Modelo CORRESPONDENCIA


class Cargo(models.Model):
	nombre_cargo = models.CharField(max_length=200)
	# history = HistoricalRecords()

	class Meta:
		verbose_name = 'cargo'
		verbose_name_plural = 'cargos'
	
	def __str__(self):
		return self.nombre_cargo

class TipoDocumento(models.Model):
	tipo_documento = models.CharField(max_length=200)
	# history = HistoricalRecords()

	class Meta:
		verbose_name = 'tipo documento'
		verbose_name_plural = 'tipos documento'

	def __str__(self):
		return self.tipo_documento

class Correspondencia(models.Model):
	codigo_hoja_ruta = models.CharField(max_length=200)
	fk_gestion = models.ForeignKey(Gestion, related_name='fk_gestion', on_delete=models.CASCADE)
	fk_usuario_oficina = models.ForeignKey(UsuarioOficina, related_name='fk_usuario_oficina',on_delete=models.CASCADE)
	numero = models.IntegerField()
	numero_oficina = models.IntegerField()
	fecha = models.DateTimeField()
	nombre = models.CharField(max_length=100)
	asunto = models.CharField(max_length=500)
	cite = models.CharField(max_length=30)
	fecha_creacion = models.DateTimeField()
	estado = models.IntegerField()
	fecha_recepcion = models.DateTimeField()
	fecha_devolucion = models.DateTimeField()
	fecha_envio = models.DateTimeField()
	enviado = models.BooleanField()
	pendiente = models.BooleanField()
	archivado = models.BooleanField()
	devuelto = models.BooleanField()
	recibido = models.BooleanField()

	class Meta:
		verbose_name = 'correspondencia'
		verbose_name_plural = 'correspondencias'
	
	def __str__(self):
		return self.codigo

# Modelo DERIVACIOONES
class Derivaciones(models.Model):
	fk_correspondencia = models.ForeignKey(Correspondencia, related_name='fk_correspondencia',on_delete=models.CASCADE)
	fecha = models.DateTimeField()
	asunto = models.CharField(max_length=500)
	remitente = models.Model(Usuarios, related_name='remitente',on_delete=models.CASCADE)
	destinatario = models.Model(Usuarios, related_name='destinatario',on_delete=models.CASCADE)
	oficina_remitente = models.ForeignKey(oficina, related_name='oficina_remitenten',on_delete=models.CASCADE)
	oficina_destino = models.ForeignKey(oficina, related_name='oficina_destino',on_delete=models.CASCADE)
	fecha_sistema = models.DateTimeField()

	class Meta:
		verbose_name = 'correspondencia'
		verbose_name_plural = 'correspondencias'
	
	def __str__(self):
		return self.fk_correspondencia





