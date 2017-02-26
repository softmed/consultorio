from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
	list_display = ('id', 'name', 'link', )
	list_filter = ('name', )