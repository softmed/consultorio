# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from datetime import date

from agenda.models import Agenda, EstadosAgenda
from users.models import Empleado, Persona

from django.views.decorators.csrf import csrf_exempt


def index_view(request):
    empleados = Empleado.objects.all()
    context = {
        'empleados' : empleados,
    }


    return render(request, 'agenda/scheduler.html', context)



def events(request):
	# eventList = Agenda.objects.select_related().values('paciente', 'paciente__persona_id__primer_nombre')
	if 'empleado_id' in request.GET and request.GET['empleado_id'] != '':
		print 'buscar por empleado_id: ' + request.GET['empleado_id']
		eventList = Agenda.objects.filter(empleado=request.GET['empleado_id']).select_related('paciente', 'empleado')
	else:
		eventList = Agenda.objects.all().select_related('paciente', 'empleado')

    
	context = {'eventList' : eventList}

	return render_to_response('agenda/event.xml', context, content_type='application/xhtml+xml')

def events_empleado(request):
	current_user = request.user
	empleado = Empleado(pk=current_user.id)

	eventList = Agenda.objects.filter(empleado=empleado.id).select_related('paciente', 'empleado')
    
	context = {'eventList' : eventList}

	return render_to_response('agenda/event.xml', context, content_type='application/xhtml+xml')


@csrf_exempt
def dataprocessor(request):
	responseList = []
	if request.method == 'POST':
		
		command = request.POST['!nativeeditor_status']
		print command
		print request.POST
		
		if command == 'inserted':
			agenda = Agenda()
			
			# procesar(request, agenda)
			current_user = request.user
			current_person = Persona(pk=current_user.id)
			current_emp = Empleado(pk=current_user.id)


			agenda.fecha_inicio = request.POST['start_date']
			agenda.fecha_fin = request.POST['end_date']
			agenda.titulo = request.POST['text']
			agenda.event_length = request.POST['event_length']
			if 'rec_type' in request.POST:
				agenda.rec_type = request.POST['rec_type']
				

			if 'event_pid' in request.POST:
				agenda.event_pid = request.POST['event_pid']

			if 'paciente_id' in request.POST and request.POST['paciente_id'] != 'null':
				agenda.paciente_id = request.POST['paciente_id']
				print 'paciente id: ' + agenda.paciente_id

			if 'empleado_id' in request.POST and request.POST['empleado_id'] != 'null' and request.POST['empleado_id'] != 'undefined':
				agenda.empleado = Empleado.objects.get(pk=request.POST['empleado_id'] )



				# agenda.empleado = request.POST['empleado_id']
				
				# e = Empleado.objects.get(pk=request.POST['empleado_id'])
				# a.usuario = e.persona
			elif current_emp:
				print "Current current_emp::::"
				print current_emp.id
				print ":::Current person"

				agenda.empleado = current_emp

			if 'estado_id' in request.POST and request.POST['estado_id'] != 'null' and request.POST['estado_id'] != 'undefined':
				agenda.estado = EstadosAgenda(pk=request.POST['estado_id'])
			
			agenda.usuario_registra = current_person

			agenda.save()


			response = {'type' : 'insert',
			    'sid': request.POST['id'],
				'tid' : agenda.id}

		elif command == 'updated':
			agenda = Agenda(pk=request.POST['id'])
			
			# procesar(request, agenda)
			current_user = request.user
			current_person = Persona(pk=current_user.id)
			current_emp = Empleado(pk=current_user.id)


			agenda.fecha_inicio = request.POST['start_date']
			agenda.fecha_fin = request.POST['end_date']
			agenda.titulo = request.POST['text']
			agenda.event_length = request.POST['event_length']
			if 'rec_type' in request.POST and request.POST['rec_type'] != 'none':
				agenda.rec_type = request.POST['rec_type']
				Agenda.objects.filter(event_pid=agenda.id).delete()

			if 'event_pid' in request.POST:
				agenda.event_pid = request.POST['event_pid']

			if 'paciente_id' in request.POST and request.POST['paciente_id'] != 'null':
				agenda.paciente_id = request.POST['paciente_id']
				print 'paciente id: ' + agenda.paciente_id

			if 'empleado_id' in request.POST and request.POST['empleado_id'] != 'null' and request.POST['empleado_id'] != 'undefined':
				agenda.empleado = Empleado.objects.get(pk=request.POST['empleado_id'] )
				# agenda.empleado = request.POST['empleado_id']

				# e = Empleado.objects.get(pk=request.POST['empleado_id'])
				# a.usuario = e.persona
			elif current_emp:
				print "Current current_emp::::"
				print current_emp.id
				print ":::Current person"

				agenda.empleado = current_emp

			if 'estado_id' in request.POST and request.POST['estado_id'] != 'null' and request.POST['estado_id'] != 'undefined':
				agenda.estado = EstadosAgenda(pk=request.POST['estado_id'])

			agenda.usuario_registra = current_person

			agenda.save()

			response = {'type' : 'update',
			    'sid': agenda.id,
				'tid' : agenda.id}

		elif command == 'deleted':
			agenda = Agenda(pk=request.POST['id'])

			if 'rec_type' in request.POST:
				Agenda.objects.filter(event_pid=agenda.id).delete()


			agenda.delete()
			response = {'type' : 'delete',
						'sid': request.POST['id'],
						'tid' : '0'}
		else:
			response = {'type' : 'error',
						'sid': request.POST['id'],
						'tid' : '0'}


	responseList.append(response)
            
	return render_to_response('agenda/dataprocessor.xml', {"responseList": responseList}, content_type="application/xhtml+xml")

def procesar(request, agenda):
	current_user = request.user
	current_person = Persona(pk=current_user.id)
	current_emp = Empleado(pk=current_user.id)


	agenda.fecha_inicio = request.POST['start_date']
	agenda.fecha_fin = request.POST['end_date']
	agenda.titulo = request.POST['text']
	agenda.event_length = request.POST['event_length']
	if 'rec_type' in request.POST:
		agenda.rec_type = request.POST['rec_type']
		Agenda.objects.filter(event_pid=agenda.id).delete()

	if 'event_pid' in request.POST:
		agenda.event_pid = request.POST['event_pid']

	if 'paciente_id' in request.POST and request.POST['paciente_id'] != 'null':
		agenda.paciente_id = request.POST['paciente_id']
		print 'paciente id: ' + agenda.paciente_id

	if 'empleado_id' in request.POST and request.POST['empleado_id'] != 'null':
		agenda.empleado = Empleado.objects.get(pk=request.POST['empleado_id'] )
		# agenda.empleado = request.POST['empleado_id']
		
		# e = Empleado.objects.get(pk=request.POST['empleado_id'])
		# a.usuario = e.persona
	elif current_emp:
		print "Current current_emp::::"
		print current_emp.id
		print ":::Current person"

		agenda.empleado = current_emp

	
	agenda.usuario_registra = current_person

	agenda.save()


def agenda_empleado(request):
	
	context = {
		'empleado':True,
	}

	return render(request, 'agenda/scheduler.html', context)


