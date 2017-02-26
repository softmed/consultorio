from django.shortcuts import render
from django.shortcuts import render_to_response

from users.models import Paciente, Empleado

from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt


def pacientes(request):
    por_nombre = True
    if 'id' in request.GET:
        pacientes = Paciente.objects.filter(pk=request.GET['id'] )
    else:
        pacientes = Paciente.objects.filter(Q(persona_id__identificacion__startswith=request.GET['mask']) 
            | Q(persona_id__primer_nombre__istartswith=request.GET['mask']) )
        por_nombre = not request.GET['mask'].isnumeric()

    context = {'pacientes' : pacientes,
                'por_nombre': por_nombre,
    }

    print context

    return render_to_response('maestras/pacientes.xml', context, content_type='application/xhtml+xml')

def empleados(request):
    
    por_nombre = True
    if 'id' in request.GET:
        empleados = Empleado.objects.filter(pk=request.GET['id'] )
    else:
        empleados = Empleado.objects.filter(Q(persona__identificacion__startswith=request.GET['mask']) 
            | Q(persona__primer_nombre__istartswith=request.GET['mask']) )
        por_nombre = not request.GET['mask'].isnumeric()

    print empleados
    context = {'empleados' : empleados,
                'por_nombre': por_nombre,
    }


    return render_to_response('maestras/empleados.xml', context, content_type='application/xhtml+xml')


@csrf_exempt
def empleados_form(request):
    empleados = Empleado.objects.all()
    context = {
        'empleados' : empleados,
    }


    return render_to_response('maestras/empleados_form.html', context)