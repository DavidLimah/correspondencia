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
class Correspondencia(models.Model):
	fk_gestion = models.ForeignKey(Gestion, related_name='fk_gestion', on_delete=models.CASCADE)
	fk_usuario_oficina = models.ForeignKey(UsuarioOficina, related_name='fk_usuario_oficina',on_delete=models.CASCADE)
	fk_oficina = models.ForeignKey(Oficina, related_name='fk_oficina',on_delete=models.CASCADE)
	

#####################################################################
# MODELOS PARA RECICLAR

# Modelos


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
	id_correspondencia = models.CharField(max_length=50)
	codigo_hoja_ruta = models.CharField(max_length=200)
	remitente = models.CharField(max_length=200)
	destinatario = models.CharField(max_length = 200)
	pendiente = models.BooleanField()
	archivado = models.BooleanField()
	devolver = models.BooleanField()
	recibido = models.BooleanField()
	comentario = models.CharField(max_length=200)
	fecha_creacion = models.DateTimeField()
	fecha_envio = models.DateTimeField()
	fecha_recepcion = models.DateTimeField()
	fecha_devolucion = models.DateTimeField()

	class Meta:
		verbose_name = 'correspondencia'
		verbose_name_plural = 'correspondencias'
	
	def __str__(self):
		return self.codigo
