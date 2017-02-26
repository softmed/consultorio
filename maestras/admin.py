from django.contrib import admin
from .models import TipoIdentificacion, Genero, EstadoCivil, Ocupacion, Rh, Color
from .models import GrupoSanguineo, Aseguradora, TipoVinculacionAseguradora
from .models import Cargo, Horario

@admin.register(TipoIdentificacion)
class AdminTipoIdentificacion(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Genero)
class AdminGenero(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(EstadoCivil)
class AdminEstadoCivil(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Ocupacion)
class AdminOcupacion(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Rh)
class AdminRh(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(GrupoSanguineo)
class AdminGrupoSanguineo(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Color)
class AdminColor(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Aseguradora)
class AdminAseguradora(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(TipoVinculacionAseguradora)
class AdminTipoVinculacionAseguradora(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Cargo)
class AdminCargo(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Horario)
class AdminHorario(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

