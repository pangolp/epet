from django.db import models
from django.contrib.auth.models import User


class Sexo(models.Model):
	nombre = models.CharField(max_length=50, help_text='Ej: Femenino')

	def __str__(self):
		return '%s' % (self.nombre)


class Documento(models.Model):
	tipo = models.CharField(max_length=9, help_text='Ej: DNI / CI, LE , LC, Pasaporte', blank=True, null=True)

	def __str__(self):
		return '%s' % (self.tipo)


class Pais(models.Model):
	nombre = models.CharField(max_length=100)


	def __str__(self):
		return '%s' % (self.nombre)


class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	segundo_apellido = models.CharField('segundo apellido', max_length=100, blank=True, null=True, help_text='campo no obligatorio')
	segundo_nombre = models.CharField('segundo nombre', max_length=50, blank=True, null=True, help_text='campo no obligatorio')
	sexo = models.OneToOneField(Sexo, on_delete=models.CASCADE)
	tipo_documento = models.OneToOneField(Documento, on_delete=models.PROTECT)
	numero_documento = models.CharField('numero de documento / pasaporte', max_length=15, help_text='Ej: 38-090879-9', blank=True, null=True)
	numero_empleado = models.CharField('numero empleado', max_length=30, blank=True, null=True)
	legajo_cpe = models.CharField('legajo CPE', max_length=50, help_text='CPE: Consejo provincial de educación', blank=True, null=True)
	observación = models.TextField(blank=True, null=True)
	pais_nacimiento = models.OneToOneField(Pais, on_delete=models.PROTECT)
	fecha_ingreso = models.DateField()
	fecha_egreso = models.DateField()

	def __str__(self):
		return '%s %s %s %s' % (self.user.lastname, self.segundo_apellido, self.user.first_name, self.segundo_nombre)