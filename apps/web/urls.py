from django.urls import path
from .views import WebIndex


app_name = 'web'
urlpatterns = [
	path('', WebIndex.as_view(), name='index'),
]
