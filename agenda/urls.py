# -*-coding:utf-8-*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # /agenda/
    url(r'^$', view=views.index_view, name='agenda'),
    url(r'^events/$', view=views.events, name='eventos'),
    url(r'^events_empleado/$', view=views.events_empleado, name='eventos'),
    url(r'^dataprocessor/$', view=views.dataprocessor, name='dataprocessor'),
    url(r'^empleado/$', view=views.agenda_empleado, name='agenda_empleado'),
]