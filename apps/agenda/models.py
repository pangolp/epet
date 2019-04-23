from django.db import models
from django.contrib.auth.models import User


class Localidad(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='localidad'
		verbose_name_plural='localidades'
		ordering = ['nombre']


class Provincia(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='provincia'
		verbose_name_plural = 'provincias'
		ordering = ['nombre']


class Libreta(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	calle = models.CharField('calle / cuadra', max_length=100)
	localidad = models.OneToOneField(Localidad, on_delete=models.PROTECT)
	provincia = models.OneToOneField(Provincia, on_delete=models.PROTECT)
	telefono_contacto = models.CharField('telefono de contacto', max_length=50)
	observación = models.TextField(blank=True, null=True)

	def __str__(self):
		return '%s %s' % (self.user.last_name, self.user.first_name)