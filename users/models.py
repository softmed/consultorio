# -*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
 
from ubicacion.models import Ciudad, Area, Sede
from maestras.models import TipoIdentificacion, EstadoCivil, Genero, Ocupacion, Color, GrupoSanguineo, Aseguradora
from maestras.models import TipoVinculacionAseguradora, Rh, Cargo, Horario



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True)
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)
    primer_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Persona(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    identificacion = models.CharField(max_length=255, null=True, unique=True)
    tipo_identificacion_id = models.ForeignKey(TipoIdentificacion, default=1)
    genero_id = models.ForeignKey(Genero, default=1)
    estado_civil_id = models.ForeignKey(EstadoCivil, default=1)

    direccion = models.CharField(max_length=255)
    ciudad_id = models.ForeignKey(Ciudad,related_name='ciudad_id', default=1)
    telefono = models.CharField(max_length=255)
    telefono_oficina = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    correo = models.EmailField(max_length=150, null=True, blank=True)

    fecha_nacimiento = models.DateField(null=True, blank=True)
    ciudad_nacimiento_id = models.ForeignKey(Ciudad, related_name='ciudad_nacimiento_id', default=1)

    ocupacion_id = models.ForeignKey(Ocupacion, default=1)
    observacion = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.primer_nombre)
    
    def __unicode__(self):
        return "%s" % (self.primer_nombre)


class Paciente(models.Model):
    persona_id = models.OneToOneField(Persona)
    grupo_sanguineo = models.ForeignKey(GrupoSanguineo, default=1)
    rh = models.ForeignKey(Rh, default=1)
    remitente = models.CharField(max_length=100, blank=True, null=True)
    aseguradora = models.ForeignKey(Aseguradora, default=1)
    tipo_vinculacion_aseguradora = models.ForeignKey(TipoVinculacionAseguradora, default=1)
#    acompanante = models.CharField(max_length=100, blank=True, null=True)
#    telefono_acompanante = models.CharField(max_length=20, null=True, blank=True)
    responsable = models.CharField(max_length=100, null=True, blank=True)
    telefono_responsable = models.CharField(max_length=20, null=True, blank=True)
    hora_nacimiento = models.TimeField(blank=True, null=True)
    registra_rips = models.BooleanField()
    def __str__(self):
        return "Paciente %s %s" % (self.persona_id.primer_nombre, self.persona_id.primer_apellido)
    
    def __unicode__(self):
        return "Paciente %s %s" % (self.persona_id.primer_nombre, self.persona_id.primer_apellido)


class EstadoEmpleado(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    persona = models.OneToOneField(Persona)
    cargo = models.ForeignKey(Cargo, default=1)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    horario = models.ForeignKey(Horario, default=1)
    area = models.ForeignKey(Area, default=1)
    sede = models.ForeignKey(Sede, default=1)
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_retiro = models.DateField(null=True, blank=True)
    estado = models.ForeignKey(EstadoEmpleado, default=1)


    def __str__(self):
        return "Paciente %s" % (self.persona.primer_nombre)
    
    def __unicode__(self):
        return "Paciente %s" % (self.persona.primer_nombre)


        