from django.contrib import admin

from .models import Localidad, Provincia, Libreta


@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Libreta)
class LibretaAdmin(admin.ModelAdmin):
	list_display = ('get_full_name', 'get_email', 'calle', 'localidad', 'provincia', 'telefono_contacto', 'observación')
	search_fields = ['telefono_contacto', 'provincia__nombre']

	"""	Como no podemos retornar directamente del usuario el apellido y el nombre, 
		debido a que una clave foránea a otra tabla, entonces utilizamos 2 funciones, 
		que retornen dichos valores y luego entonces si tenemos acceso a esa información que queríamos.
		De ultima manera con el e-mail, para completar la libreta.
	"""
	def get_full_name(self, obj):
		return '%s %s' % (obj.user.last_name, obj.user.first_name)
	get_full_name.short_description = 'Nombre completo'

	def get_email(self, obj):
		return '%s' % (obj.user.email)
	get_email.short_description = 'E-mail'
