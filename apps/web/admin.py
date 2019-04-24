from django.contrib import admin

from .models import Categoria, Novedad, Cargo, Institucional



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'categoria', 'fecha_publicación', 'modificado', 'user')

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'orden')


@admin.register(Institucional)
class InstitucionalAdmin(admin.ModelAdmin):
	list_display = ('cargo', 'nombre', 'apellido', 'anexo', 'foto', 'sitio_web', 'info')
