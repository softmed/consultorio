from __future__ import unicode_literals


from django.db import models
from maestras.models import Horario

class Pais(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre
	
	class Meta:
		verbose_name_plural = 'Paises'


class Departamento(models.Model):
	nombre = models.CharField(max_length=100)
	pais = models.ForeignKey(Pais)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Departamentos'

class Ciudad(models.Model):
	nombre = models.CharField(max_length=100)
	departamento = models.ForeignKey(Departamento)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Ciudades'

class Area(models.Model):
	nombre = models.CharField(max_length=100)
	
	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Areas'

class Sede(models.Model):
	nombre = models.CharField(max_length=100)
	ciudad = models.ForeignKey(Ciudad)
	
	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Sedes'


class TipoUbicacion(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Tipos de Ubicacion'



class Ubicacion(models.Model):
	nombre = models.CharField(max_length=100)
	sede = models.ForeignKey(Sede)
	tipo = models.ForeignKey(TipoUbicacion)
	estado = models.BooleanField()
	horario = models.ForeignKey(Horario, blank=True, null=True)

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Ubicaciones'









