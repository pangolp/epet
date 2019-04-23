from django.urls import path
from .views import WebIndex, NovedadDetalle


app_name = 'web'
urlpatterns = [
	path('', WebIndex.as_view(), name='index'),
	path('novedad/<str:slug>/', NovedadDetalle.as_view(), name='novedad_id'),
]
