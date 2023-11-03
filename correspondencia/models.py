from django.db import models

# Modelos
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
	
	def __str__(self):
		return self.codigo


class Oficina(models.Model):
	nombre_oficina = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre_oficina


class Cargo(models.Model):
	nombre_cargo = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre_cargo

