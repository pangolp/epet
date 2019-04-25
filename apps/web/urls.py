from django.urls import path
from .views import (
	WebIndex,
	NovedadDetalle,
	AutoridadesView,
	AutoridadDetail,
	TallerView,
	AlumnoView
)

app_name = 'web'
urlpatterns = [
	path('', WebIndex.as_view(), name='index'),
	path('novedad/<str:slug>/', NovedadDetalle.as_view(), name='novedad_id'),
	path('autoridades/', AutoridadesView.as_view(), name='autoridades'),
	path('autoridad/<int:pk>/', AutoridadDetail.as_view(), name='autoridad_detalle'),

	# Taller
	path('taller/', TallerView.as_view(), name='taller'),
	# Alumnos
	path('alumnos/', AlumnoView.as_view(), name='alumnos'),
]
