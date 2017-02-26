from django.contrib import admin

from models import EstadosAgenda

@admin.register(EstadosAgenda)
class AdminEstadosAgenda(admin.ModelAdmin):
	list_display = ('id', 'nombre', )
