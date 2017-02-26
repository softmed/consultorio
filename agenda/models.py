from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from users.models import Paciente, Persona, Empleado

class EstadosAgenda(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Estados Agenda'

class Agenda(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, blank=True, null=True)
    observacion = models.TextField(max_length=255, blank=True, null=True)
    usuario_registra = models.ForeignKey(Persona, related_name='usario_registra')
    paciente = models.ForeignKey(Paciente, blank=True, null=True)
    rec_type = models.CharField(max_length=20, blank=True, null=True)
    event_length = models.CharField(max_length=20, blank=True, null=True)
    event_pid = models.CharField(max_length=6, blank=True, null=True)
    estado = models.ForeignKey(EstadosAgenda, blank=True, null=True)

    #ubicacion = 
	#recordatorio = 