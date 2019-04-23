from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Novedad


class WebIndex(ListView):
	queryset = Novedad.objects.order_by('-fecha_publicación')[:5]
	template_name = 'web/index.html'
	context_object_name = 'novedades'