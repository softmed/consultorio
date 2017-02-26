
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TipoIdentificacion(models.Model):
	nombre = models.CharField(max_length=50)
	sigla = models.CharField(max_length=15)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Tipos de Identificación'

class Genero(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Generos'


class EstadoCivil(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Estados Civiles'

class Ocupacion(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Ocupaciones'

class Rh(models.Model):
	nombre = models.CharField(max_length=8)
	signo = models.CharField(max_length=1)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.signo

	class Meta:
		verbose_name_plural = 'RHs'


class GrupoSanguineo(models.Model):
	nombre = models.CharField(max_length=2)
	

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Grupos Sanguineos'


class Color(models.Model):
	nombre = models.CharField(max_length=50)


	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Colores'

class Aseguradora(models.Model):
	nombre = models.CharField(max_length=50)


	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Aseguradoras'


class TipoVinculacionAseguradora(models.Model):
	nombre = models.CharField(max_length=50)


	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = 'Tipos de Vinculacion con Aseguradora'


class Cargo(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre	

	class Meta:
		verbose_name_plural = 'Cargos'

class Horario(models.Model):
	nombre = models.CharField(max_length=50)

	lunes = models.CharField(max_length=100, blank=True, null=True)
	martes = models.CharField(max_length=100, blank=True, null=True)
	miercoles = models.CharField(max_length=100, blank=True, null=True)
	jueves = models.CharField(max_length=100, blank=True, null=True)
	viernes = models.CharField(max_length=100, blank=True, null=True)
	sabado = models.CharField(max_length=100, blank=True, null=True)
	domingo = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre	

	class Meta:
		verbose_name_plural = 'Horarios'




