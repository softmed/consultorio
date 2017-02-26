# -*-coding:utf-8-*-
from __future__ import unicode_literals


from django import forms
from django.contrib.auth.models import User
from models import Persona, Paciente, Empleado


from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import FormActions, PrependedText, AppendedText
from crispy_forms.layout import LayoutObject, Submit, HTML


class RegistroUserForm(forms.Form):

	username = forms.CharField(
    	min_length=5,
    	widget=forms.TextInput(attrs={'class': 'form-control'}))

	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'class': 'form-control'}))

	password = forms.CharField(
	    min_length=5,
	    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	password2 = forms.CharField(
	    min_length=5,
	    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	photo = forms.ImageField(required=False)

	def clean_username(self):
		"""Comprueba que no exista un username igual en la db"""
		username = self.cleaned_data['username']
		if User.objects.filter(username=username):
			raise forms.ValidationError('Nombre de usuario ya registrado.')
		return username

	def clean_email(self):
		"""Comprueba que no exista un email igual en la db"""
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('Ya existe un email igual en la db.')
		return email

	def clean_password2(self):
	    """Comprueba que password y password2 sean iguales."""
	    password = self.cleaned_data['password']
	    password2 = self.cleaned_data['password2']
	    if password != password2:
	        raise forms.ValidationError('Las contraseñas no coinciden.')
	    return password2


class PersonaFormOriginal(forms.ModelForm):
	class Meta:
		model = Persona
		exclude = ('user_id', )
		#fields = ['primer_nombre', 'primer_apellido']
		"""exclude = []
		widgets = {
    		'primer_nombre': forms.TextInput(attrs={'placeholder': 'primer_nombre'}),
    	}"""

	def __init__(self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)

		self.fields['primer_nombre'].label = 'Primer Nombre'
		self.fields['tipo_identificacion_id'].label = 'Tipo de Identificacion'
		self.fields['genero_id'].label = 'Genero'
		self.fields['estado_civil_id'].label = 'Estado civil'
		self.fields['ciudad_id'].label = 'Ciudad'
		self.fields['correo'].label = 'Correo Electrónico'
		self.fields['ciudad_nacimiento_id'].label = 'Ciudad de Nacimiento'
		self.fields['ocupacion_id'].label = 'Ocupacion'
		
		self.helper = FormHelper()
		self.helper.form_tag = False
		#self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'POST'
		self.helper.label_class = 'col-xs-2 col-form-label'
		self.helper.field_class = 'col-xs-6'

		


		#enctype="multipart/form-data"

		self.helper.layout = layout.Layout(
			layout.Fieldset(
				'Informacion Personal',
				
				layout.Field('tipo_identificacion_id', placeholder='', wrapper_class='row'),
				layout.Field('identificacion', placeholder='', wrapper_class='row'),
				layout.Field('primer_nombre', placeholder='', wrapper_class='row'),
				layout.Field('segundo_nombre', placeholder='', wrapper_class='row'),
				layout.Field('primer_apellido', placeholder='', wrapper_class='row'),
				layout.Field('segundo_apellido', placeholder='', wrapper_class='row'),
				
				layout.Field('genero_id', placeholder='', wrapper_class='row'),
				layout.Field('estado_civil_id', placeholder='', wrapper_class='row'),
			
			),			
			layout.Fieldset(
				'Datos de Contacto',
				layout.Field('direccion', placeholder='', wrapper_class='row'),
				layout.Field('ciudad_id', placeholder='', wrapper_class='row'),
				layout.Field('telefono', placeholder='', wrapper_class='row'),
				layout.Field('telefono_oficina', placeholder='', wrapper_class='row'),
				layout.Field('celular', placeholder='', wrapper_class='row'),
				layout.Field('correo', placeholder='correo@example.com', wrapper_class='row'),
				
			),
			layout.Fieldset(
				'Otros Datos',
				layout.Field('fecha_nacimiento', placeholder='dd/mm/yyyy', css_class='dateinput', wrapper_class='row'),
				layout.Field('ciudad_nacimiento_id', placeholder='', wrapper_class='row'),
				layout.Field('ocupacion_id', placeholder='', wrapper_class='row'),
				layout.Field('observacion', placeholder='', wrapper_class='row'),
				
				
			),
		)
import random
# Con el formulario lleno para pruebas
class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		exclude = ('user_id', )
		#fields = ['primer_nombre', 'primer_apellido']
		"""exclude = []
		widgets = {
    		'primer_nombre': forms.TextInput(attrs={'placeholder': 'primer_nombre'}),
    	}"""

	def __init__(self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)

		self.fields['primer_nombre'].label = 'Primer Nombre'
		self.fields['tipo_identificacion_id'].label = 'Tipo de Identificacion'
		self.fields['genero_id'].label = 'Genero'
		self.fields['estado_civil_id'].label = 'Estado civil'
		self.fields['ciudad_id'].label = 'Ciudad'
		self.fields['correo'].label = 'Correo Electrónico'
		self.fields['ciudad_nacimiento_id'].label = 'Ciudad de Nacimiento'
		self.fields['ocupacion_id'].label = 'Ocupacion'
		
		self.helper = FormHelper()
		self.helper.form_tag = False
		#self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'POST'
		self.helper.label_class = 'col-xs-2 col-form-label'
		self.helper.field_class = 'col-xs-6'

		


		#enctype="multipart/form-data"

		self.helper.layout = layout.Layout(
			layout.Fieldset(
				'Informacion Personal',
				
				layout.Field('tipo_identificacion_id', placeholder='', wrapper_class='row'),
				layout.Field('identificacion', placeholder='', wrapper_class='row', value=str(random.randint(1000000000,99999999999))),
				layout.Field('primer_nombre', placeholder='', wrapper_class='row', value='Test' + str(random.randint(100,999))),
				layout.Field('segundo_nombre', placeholder='', wrapper_class='row'),
				layout.Field('primer_apellido', placeholder='', wrapper_class='row', value='ApeTest' + str(random.randint(100,999))),
				layout.Field('segundo_apellido', placeholder='', wrapper_class='row'),
				
				layout.Field('genero_id', placeholder='', wrapper_class='row'),
				layout.Field('estado_civil_id', placeholder='', wrapper_class='row'),
			
			),			
			layout.Fieldset(
				'Datos de Contacto',
				layout.Field('direccion', placeholder='', wrapper_class='row', value='dir prueba'),
				layout.Field('ciudad_id', placeholder='', wrapper_class='row'),
				layout.Field('telefono', placeholder='', wrapper_class='row', value='tel prueba'),
				layout.Field('telefono_oficina', placeholder='', wrapper_class='row'),
				layout.Field('celular', placeholder='', wrapper_class='row'),
				layout.Field('correo', placeholder='correo@example.com', wrapper_class='row'),
				
			),
			layout.Fieldset(
				'Otros Datos',
				layout.Field('fecha_nacimiento', placeholder='dd/mm/yyyy', css_class='dateinput', wrapper_class='row'),
				layout.Field('ciudad_nacimiento_id', placeholder='', wrapper_class='row'),
				layout.Field('ocupacion_id', placeholder='', wrapper_class='row'),
				layout.Field('observacion', placeholder='', wrapper_class='row'),
				
				
			),
		)


		"""
		#AppendedText('segundo_nombre','@')
		self.helper.layout.append(
			FormActions(
				layout.Submit('save', 'Guardar'),
				layout.Button('cancel', 'Cancelar')
			)
		)
		"""





		"""
		self.helper.layout.append(
			FormActions(
				layout.HTML('<a role="button" class="btn btn-default" href="">Cancel</a>'),
				layout.Submit('save', 'Submit'),
				layout.Button('cancel', 'Cancel'),
			)
		)

		self.helper.layout.append(
			AppendedText('segundo_nombre','@')
		)

		"""
		#self.request = kwargs.pop('request', None)
		#return 
		"""
		super(PersonaForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_action = ""
		self.helper.form_method = "POST"

		#self.fields["bulletin_type"].widget = forms.RadioSelect()


		self.helper.layout = layout.Layout(
			layout.Fieldset(
				"Main data",
				#layout.Field("primer_nombre", css_class="input-block-level"),
				#layout.Field("primer_apellido")
				'primer_nombre',
				'primer_apellido'
			)
		)


		"""
#		self.helper.layout.append(
#			FormActions(
#				HTML("""<a role="button" class="btn btn-default"
#					href="{% url "some_cancel_url" %}">Cancel</a>"""),
#				Submit('save', 'Submit'),
#		))



"""    	
    	
	def __init__(self, *args, **kwargs):
		super(MyForm, self).__init__(*args, **kwargs)
		for key, field in self.fields.items():
			if isinstance(field.widget, forms.TextInput) or \
 				isinstance(field.widget, forms.Textarea) or \
				isinstance(field.widget, forms.DateInput) or \
				isinstance(field.widget, forms.DateTimeInput) or \
				isinstance(field.widget, forms.TimeInput):
				field.widget.attrs.update({'placeholder': field.label})
"""

class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		exclude = ('persona_id', )

	def __init__(self, *args, **kwargs):
		super(PacienteForm, self).__init__(*args, **kwargs)

		
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.label_class = 'col-xs-2 col-form-label'
		self.helper.field_class = 'col-xs-6'		
		self.helper.form_tag = False


		self.helper.layout = layout.Layout(
			layout.Fieldset(
				'Datos del Paciente',
				
				layout.Field('hora_nacimiento', placeholder='', wrapper_class='row'),
				layout.Field('grupo_sanguineo', placeholder='', wrapper_class='row'),
				layout.Field('rh', placeholder='', wrapper_class='row'),
				layout.Field('remitente', placeholder='', wrapper_class='row'),
				layout.Field('aseguradora', placeholder='', wrapper_class='row'),
				layout.Field('tipo_vinculacion_aseguradora', placeholder='', wrapper_class='row'),
				layout.Field('responsable', placeholder='', wrapper_class='row'),
				layout.Field('telefono_responsable', placeholder='', wrapper_class='row'),
				layout.Field('registra_rips', placeholder='', wrapper_class='row'),
			
			),
		)

		#AppendedText('segundo_nombre','@')
		self.helper.layout.append(
			FormActions(
				layout.Submit('save', 'Guardar'),
				
			)
		)

	
class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		exclude = ('persona', )

	def __init__(self, *args, **kwargs):
		super(EmpleadoForm, self).__init__(*args, **kwargs)

		
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.label_class = 'col-xs-2 col-form-label'
		self.helper.field_class = 'col-xs-6'		
		self.helper.form_tag = False


		self.helper.layout = layout.Layout(
			layout.Fieldset(
				'Datos del Empleado',
				
				layout.Field('fecha_ingreso', placeholder='dd/mm/yyyy', css_class='dateinput', wrapper_class='row'),
				layout.Field('fecha_retiro', placeholder='dd/mm/yyyy', css_class='dateinput', wrapper_class='row'),
				layout.Field('area', placeholder='', wrapper_class='row'),
				layout.Field('cargo', placeholder='', wrapper_class='row'),
				layout.Field('estado', placeholder='', wrapper_class='row'),
				layout.Field('horario', placeholder='', wrapper_class='row'),
				layout.Field('persona', placeholder='', wrapper_class='row'),
				layout.Field('sede', placeholder='', wrapper_class='row'),
				layout.Field('salario', placeholder='', wrapper_class='row'),
			
			),
		)

		#AppendedText('segundo_nombre','@')
		self.helper.layout.append(
			FormActions(
				layout.Submit('save', 'Guardar'),
				
			)
		)

	
