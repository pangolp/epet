from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField

class Categoria(models.Model):

	nombre = models.CharField(max_length=50, help_text='Ej. Profesores')

	def __str__(self):
		return '%s' % (self.nombre)


class Novedad(models.Model):
	
	titulo = models.CharField(max_length=50)
	subtitulo = models.CharField(max_length=255, help_text='Lo que se va a ver en la página principal')
	cuerpo = RichTextField()
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
	# auto_now_add = La próxima vez que se genera se le asigna una fecha
	fecha_publicación = models.DateTimeField(auto_now_add=True)
	# auto_now = Cada vez que se modifica, se le carga la nueva fecha.
	modificado = models.DateTimeField(auto_now=True)
	# Es un campo oculto, no puede ser modificado por el usuario.
	slug = models.SlugField(max_length=50, editable=False, blank=True, null=True)
	user = models.ForeignKey(User, editable=False, on_delete=models.PROTECT)

	"""
	Sobrescribimos el método save,
	para que cada vez que se guarde la publicación,
	convierta el titulo y el resumen en mayúscula.
	Se a lo que el usuario ingrese en el formulario,
	siempre se va a guardar en minúsculas en la base de datos.
	"""

	def __str__(self):
		return '%s' % (self.titulo)

	def save(self):
		self.titulo = self.titulo.lower()
		self.subtitulo = self.subtitulo.lower()
		self.slug = slugify(self.titulo.lower())
		super(Novedad, self).save()

	class Meta:
		verbose_name='novedad'
		verbose_name_plural = 'novedades'


class Cargo(models.Model):
	nombre = models.CharField(max_length=50, help_text='Director')
	orden = models.PositiveSmallIntegerField(help_text='Orden en que se muestran')

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		verbose_name='cargo'
		verbose_name_plural = 'cargos'
		ordering = ['orden']

class Institucional(models.Model):
	cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	anexo = models.CharField(max_length=150, help_text='Regente de Cultura Técnica T.T.', blank=True, null=True)
	foto = models.ImageField(upload_to='institucional/perfil', default='institucional/perfil/no-img.png')
	sitio_web = models.URLField('sitio web', blank=True, null=True)
	info = RichTextField(blank=True, null=True, help_text='Mas información')

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)

	class Meta:
		verbose_name='institucional'
		verbose_name_plural='autoridades'
		ordering = ['cargo']