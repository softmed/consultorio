# -*-coding:utf-8-*-
from __future__ import unicode_literals
"""from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def authentication(request):
	if request.method == 'POST':
		# valor que viene por POST en el request
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		if action == 'signup':
			user = User.objects.create_user(username=username, password=password)
			user.save()
		elif action == 'login':
			user = authenticate(username=username, password=password)

			login(request, user)
		return redirect('/')

	return render(request, 'login.html', {})"""
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import RegistroUserForm
from .models import UserProfile
from .models import Persona, Paciente, Empleado

from django.views.generic import CreateView, DetailView, ListView, UpdateView

from django.template.response import TemplateResponse

from django.http import HttpResponseRedirect


from django.db.models import Q


def registro_usuario_view(request):
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = RegistroUserForm(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            photo = cleaned_data.get('photo')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # Añadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # y le asignamos la photo (el campo, permite datos null)
            user_profile.photo = photo
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina accounts/gracias.html
            # Pero lo hacemos con un redirect.
            return redirect(reverse('users:gracias', kwargs={'username': username}))
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = RegistroUserForm()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'users/registro.html', context)


def registro_paciente_view(request):
    if request.method == 'POST':
            return redirect(reverse('users:gracias', kwargs={'username': username}))
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = PersonaForm()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'users/registro.html', context)    

@login_required
def gracias_view(request, username):
    return render(request, 'users/gracias.html', {'username': username})


@login_required
def index_view(request):
    return render(request, 'users/index.html')


def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('users:index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
		    	    return redirect(request.GET.get('next'))
                return redirect(reverse('users:index'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        mensaje = 'Nombre de usuario o contraseña no valido'
    return render(request, 'users/login.html', {'mensaje': mensaje})

def logout_view(request, next_page):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    #return redirect(reverse('users:login'))
    return redirect(next_page)

from .forms import PersonaForm, PacienteForm, EmpleadoForm



class PacienteCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    second_form_class = PacienteForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        form = PersonaForm(request.POST, request.FILES)
        form2 = PacienteForm(request.POST, request.FILES)
        #form = self.form_class(request.POST)

        print form


        if form.is_valid():
            print "Is valid!!!"
            test_name = form.cleaned_data['primer_nombre']

        if form.is_valid() and form2.is_valid():
            userdata = form.save(commit=False)
            userdata.save()
            pacientedata = form2.save(commit=False)
            pacientedata.persona_id = userdata
            pacientedata.save()
            messages.success(self.request, 'Se crea el paciente %s %s satisfactoriamente' % ( form.cleaned_data['primer_nombre'], form.cleaned_data['primer_apellido']))
            return HttpResponseRedirect('/users/nuevo_paciente')
            #return HttpResponseRedirect('/users/actualiza_paciente/%s' % (pacientedata.id))




        context = {
                'titulo': 'Paciente',
                'form':    form,
                'form2': form2,
            }

        return render(request, 'users/persona_form.html', context)

    def get(self, request, *args, **kwargs):
        super(PacienteCreate, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form, form2=form2, titulo='Paciente'))

class PacienteCreatePopup(CreateView):
    model = Persona
    form_class = PersonaForm
    second_form_class = PacienteForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        form = PersonaForm(request.POST, request.FILES)
        form2 = PacienteForm(request.POST, request.FILES)
        #form = self.form_class(request.POST)

        print form


        if form.is_valid():
            print "Is valid!!!"
            test_name = form.cleaned_data['primer_nombre']

        if form.is_valid() and form2.is_valid():
            userdata = form.save(commit=False)
            userdata.save()
            pacientedata = form2.save(commit=False)
            pacientedata.persona_id = userdata
            pacientedata.save()
            #return HttpResponseRedirect('/users/nuevo_paciente')
            return render(request, 'users/nuevo_paciente_close.html', {'valor':form.cleaned_data['identificacion'] +" | " + form.cleaned_data['primer_nombre'], 'id': pacientedata.id})
            #return HttpResponseRedirect('/users/actualiza_paciente/%s' % (pacientedata.id))

        context = {
                'titulo': 'Paciente',
                'form':    form,
                'form2': form2,
                'popup': True
            }

        return render(request, 'users/persona_form.html', context)

    def get(self, request, *args, **kwargs):
        super(PacienteCreatePopup, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form, form2=form2, popup=True, titulo='Paciente'))

class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    second_form_class = PersonaForm
    #context['form'] = self.form_class(self.request.GET, instance=request.user)
    success_url = '/'
    
    def get_object(self, queryset=None):
        print "Obtener Objeto!!!!!!!!"
        obj = Paciente.objects.get(id=self.kwargs['id'])
        print obj.persona_id.primer_nombre
        return obj
    

    def post(self, request, *args, **kwargs):
        #self.object = self.get_object()
        form = PacienteForm(request.POST, request.FILES, instance=self.get_object())


        form2 = PersonaForm(request.POST, request.FILES, instance=self.get_object().persona_id)
        
        #form = self.form_class(request.POST)
    
        if form.is_valid() and form2.is_valid():
            print "\n"*5
            print "validooooo"
            
            userdata = form2.save(commit=False)

            #print userdata

            #userdata.save()
            userdata.save()
            pacientedata = form.save(commit=False)
            pacientedata.persona_id = userdata
            pacientedata.save()
            messages.success(self.request, 'Se actualiza el paciente %s %s satisfactoriamente' % ( form2.cleaned_data['primer_nombre'], form2.cleaned_data['primer_apellido']))
            #return HttpResponseRedirect('/users/nuevo_paciente')
            return HttpResponseRedirect('/users/actualiza_paciente/%s' % (pacientedata.id))
            #return render(request, 'users/paciente_form.html', context)


        context = {
                'form':    form,
                'form2': form2,
            }

        return render(request, 'users/paciente_form.html', context)



    def get_context_data(self, **kwargs):
        context = super(PacienteUpdate, self).get_context_data(**kwargs)
        if 'form' not in context:
            #context['form'] = self.form_class
            context['form'] = self.form_class(self.request.GET, instance=request.persona)
        #print context['form'] 
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.object.persona_id)
            #context['form2'] = self.second_form_class(instance=self.get_object().persona_id)
            #context['form2'] = self.form_class(self.request.GET, instance=request.persona)
        print "\n"*4
        print context['form2'] 



        return context

     
class PacienteList(ListView):
    model = Paciente
    paginate_by = 10
    filtro = ""
    

    def post(self, request, *args, **kwargs):
        print request.POST['bus_id']
        #query = super(PacienteList, self).get_queryset()
        #query.filter(persona_id__primer_nombre=request.POST['bus_id'])
        #return TemplateResponse(self.request, 'users/persona_form.html', None)
        self.filtro = request.POST['bus_id']
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)



    def get_queryset(self):
        query = super(PacienteList, self).get_queryset()
        if self.filtro != "":
            #return query.filter(persona_id__primer_nombre__icontains=self.filtro)
            # return query.filter(Q(persona_id__primer_nombre__icontains=self.filtro) 
            #     | Q(persona_id__segundo_nombre__icontains=self.filtro)
            #     | Q(persona_id__primer_apellido__icontains=self.filtro) 
            #     | Q(persona_id__segundo_apellido__icontains=self.filtro) )
            return query.filter(Q(persona_id__identificacion__icontains=self.filtro))
        else:
            return query



##### Empleados


class EmpleadoCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    second_form_class = EmpleadoForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        form = PersonaForm(request.POST, request.FILES)
        form2 = EmpleadoForm(request.POST, request.FILES)
       
        if form.is_valid() and form2.is_valid():
            userdata = form.save(commit=False)
            userdata.save()
            empleadodata = form2.save(commit=False)
            empleadodata.persona = userdata
            empleadodata.save()
            messages.success(self.request, 'Se crea el empleado %s %s satisfactoriamente' % ( form.cleaned_data['primer_nombre'], form.cleaned_data['primer_apellido']))
            return HttpResponseRedirect('/users/nuevo_empleado')
           



        context = {
                'titulo': 'Empleado',
                'form': form,
                'form2': form2,
            }

        return render(request, 'users/persona_form.html', context)

    def get(self, request, *args, **kwargs):
        super(EmpleadoCreate, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form, form2=form2, titulo='Empleado'))

class EmpleadoCreatePopup(CreateView):
    model = Persona
    form_class = PersonaForm
    second_form_class = EmpleadoForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        form = PersonaForm(request.POST, request.FILES)
        form2 = EmpleadoForm(request.POST, request.FILES)
      
        if form.is_valid() and form2.is_valid():
            userdata = form.save(commit=False)
            userdata.save()
            empleadodata = form2.save(commit=False)
            empleadodata.persona = userdata
            empleadodata.save()
            return render(request, 'users/nuevo_empleado_close.html', {'valor':form.cleaned_data['identificacion'] +" | " + form.cleaned_data['primer_nombre'], 'id': empleadodata.id})

        context = {
                'titulo': 'Empledado',
                'form':    form,
                'form2': form2,
                'popup': True
            }

        return render(request, 'users/empleado_form.html', context)

    def get(self, request, *args, **kwargs):
        super(EmpleadoCreatePopup, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form, form2=form2, popup=True, titulo='Empleado'))

class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    second_form_class = PersonaForm
    #context['form'] = self.form_class(self.request.GET, instance=request.user)
    success_url = '/'
    
    def get_object(self, queryset=None):
        print "Obtener Objeto!!!!!!!!"
        obj = Empleado.objects.get(id=self.kwargs['id'])
        return obj
    

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST, request.FILES, instance=self.get_object())
        form2 = PersonaForm(request.POST, request.FILES, instance=self.get_object().persona)
        
        if form.is_valid() and form2.is_valid():
            userdata = form2.save(commit=False)
            userdata.save()
            empleadodata = form.save(commit=False)
            empleadodata.persona = userdata
            empleadodata.save()
            messages.success(self.request, 'Se actualiza el epleado %s %s satisfactoriamente' % ( form2.cleaned_data['primer_nombre'], form2.cleaned_data['primer_apellido']))
            return HttpResponseRedirect('/users/actualiza_empleado/%s' % (empleadodata.id))

        context = {
                'form':    form,
                'form2': form2,
            }

        return render(request, 'users/empleado_form.html', context)



    def get_context_data(self, **kwargs):
        context = super(EmpleadoUpdate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET, instance=request.persona)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=self.object.persona)

        context['titulo'] = 'Empleado'
        return context

     
class EmpleadoList(ListView):
    model = Empleado
    paginate_by = 10
    filtro = ""
    

    def post(self, request, *args, **kwargs):
        self.filtro = request.POST['bus_id']
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)



    def get_queryset(self):
        query = super(EmpleadoList, self).get_queryset()
        if self.filtro != "":
            #return query.filter(persona_id__primer_nombre__icontains=self.filtro)
            return query.filter(Q(persona__primer_nombre__icontains=self.filtro) 
                | Q(persona__segundo_nombre__icontains=self.filtro)
                | Q(persona__primer_apellido__icontains=self.filtro) 
                | Q(persona__segundo_apellido__icontains=self.filtro) )
        else:
            return query

