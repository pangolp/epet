from django.shortcuts import render
from django.views.generic import TemplateView


class WebIndex(TemplateView):
	template_name = 'web/index.html'