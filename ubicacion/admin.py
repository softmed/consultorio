from django.contrib import admin
from .models import Ciudad, Departamento, Pais, Area, Sede, Ubicacion, TipoUbicacion


@admin.register(Ciudad)
class AdminCiudad(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'departamento', )

@admin.register(Pais)
class AdminCiudad(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'descripcion', )

@admin.register(Departamento)
class AdminCiudad(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'pais', )

@admin.register(Area)
class AdminArea(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Sede)
class AdminSede(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(TipoUbicacion)
class AdminTipoUbicacion(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

@admin.register(Ubicacion)
class AdminTipoUbicacion(admin.ModelAdmin):
	list_display = ('id', 'nombre', )

