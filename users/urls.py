# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views

# Añade esto, al inicio del documento
from django.conf import settings

# Para agregar el logout
from django.contrib.auth import views as auth_views

urlpatterns = [
		url(r'^$', views.index_view, name='index'),
    	url(r'^login/$', views.login_view, name='login'),
		url(r'^registro/$', views.registro_usuario_view, name='registro'),
        url(r'^nuevo_paciente/$', views.PacienteCreate.as_view(), name='nuevo_paciente'),
        url(r'^nuevo_paciente/popup$', views.PacienteCreatePopup.as_view(), name='nuevo_paciente_popup'),
        url(r'^lista_pacientes/$', views.PacienteList.as_view(), name='lista_pacientes'),
        url(r'^nuevo_empleado/$', views.EmpleadoCreate.as_view(), name='nuevo_empleado'),
        url(r'^nuevo_empleado/popup$', views.EmpleadoCreatePopup.as_view(), name='nuevo_empleado_popup'),
        url(r'^lista_empleados/$', views.EmpleadoList.as_view(), name='lista_empleados'),
        url(r'^actualiza_paciente/(?P<id>[0-9]+)/$', views.PacienteUpdate.as_view(), name='actualiza_paciente'),
        url(r'^actualiza_empleado/(?P<id>[0-9]+)/$', views.EmpleadoUpdate.as_view(), name='actualiza_empleado'),
        url(r'^registro_paciente/$', views.registro_paciente_view, name='registro_paciente'),
        #url(r'^login/$', views.authentication, name='login'),
        url(r'^logout$', views.logout_view, {'next_page': '/users/login'}, name='logout'),
        #url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
        url(r'gracias/(?P<username>[\w]+)/', views.gracias_view, name='gracias'),

]
# Añade esto, al final del documento
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(
        # /media/:<mixed>path/
        url(
            regex=r'^media/(?P<path>.*)$',
            view='django.views.static.serve',
            kwargs={'document_root': settings.MEDIA_ROOT}))