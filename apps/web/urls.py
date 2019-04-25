from django.urls import path
from .views import WebIndex,NovedadDetalle, AutoridadesView, AutoridadDetail


app_name = 'web'
urlpatterns = [
	path('', WebIndex.as_view(), name='index'),
	path('novedad/<str:slug>/', NovedadDetalle.as_view(), name='novedad_id'),
	path('autoridades/', AutoridadesView.as_view(), name='autoridades'),
	path('autoridad/<int:pk>/', AutoridadDetail.as_view(), name='autoridad_detalle'),
]
