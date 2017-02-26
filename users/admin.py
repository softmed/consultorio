from django.contrib import admin
from .models import UserProfile
from .models import Persona, Paciente, Empleado, EstadoEmpleado

@admin.register(UserProfile)
class AdminUsersProfiles(admin.ModelAdmin):
	list_display = ('id', 'user', 'photo', )
	list_filter = ('user', )

@admin.register(Persona)
class AdminPersona(admin.ModelAdmin):
	list_display = ('id', 'primer_nombre', )

@admin.register(Paciente)
class AdminPaciente(admin.ModelAdmin):
	list_display = ('id', 'persona_id',)

@admin.register(Empleado)
class AdminEmpleado(admin.ModelAdmin):
	list_display = ('id', 'persona_id',)

@admin.register(EstadoEmpleado)
class AdminEstadoEmpleado(admin.ModelAdmin):
	list_display = ('id', 'nombre',)

