from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

"""from menu.models import Menu

def home(request):
	menus = Menu.objects.order_by('id')
    	template = loader.get_template('home.html')
    	context = {
      		'menus': menus
    	}
    	return HttpResponse(template.render(context, request))
"""
from django.views.generic import TemplateView

from braces.views import GroupRequiredMixin


class About(GroupRequiredMixin, TemplateView):
	template_name = 'about.html'
    #required
	group_required = (u"auxiliar",)


