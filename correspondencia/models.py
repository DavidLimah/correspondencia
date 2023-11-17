from django.db import models

# from simple_history.models import HistoricalRecords

# Modelos
class Oficina(models.Model):
	nombre_oficina = models.CharField(max_length=200)
	# history = HistoricalRecords()

	class Meta:
		verbose_name = 'oficina'
		verbose_name_plural = 'oficinas'
	
	def __str__(self):
		return self.nombre_oficina

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


"""
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
"""