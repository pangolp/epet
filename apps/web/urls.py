from django.urls import path
from .views import WebIndex, NovedadDetalle


app_name = 'web'
urlpatterns = [
	path('', WebIndex.as_view(), name='index'),
	path('novedad/<int:pk>/', NovedadDetalle.as_view(), name='novedad_id'),
]
