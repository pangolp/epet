from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .models import Novedad, Institucional


class WebIndex(ListView):
	queryset = Novedad.objects.order_by('-fecha_publicación')[:5]
	template_name = 'web/index.html'
	context_object_name = 'novedades'


class NovedadDetalle(DetailView):
	model = Novedad
	template_name = 'web/novedad/novedaddetalle.html'
	context_object_name = 'novedad'


class AutoridadesView(ListView):
	model = Institucional
	template_name = 'web/institucional/autoridades.html'
	context_object_name = 'autoridades'


class AutoridadDetail(DetailView):
	model = Institucional
	template_name = 'web/institucional/autoridad_detalle.html'
	context_object_name = 'autoridad'


class TallerView(TemplateView):
	template_name = 'web/taller/taller_index.html'


class AlumnoView(TemplateView):
	template_name = 'web/alumnos/alumnos_index.html'