# -*-coding:utf-8-*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # /agenda/
    #url(r'^$', view=views.index_view, name='agenda'),
    url(r'^pacientes/$', view=views.pacientes, name='pacientes'),
    url(r'^empleados/$', view=views.empleados, name='empleados'),
    url(r'^empleados_form/$', view=views.empleados_form, name='empleados_form'),
]