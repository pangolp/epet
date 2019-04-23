from django.contrib import admin

from .models import Categoria, Novedad



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):

	list_display = ('titulo', 'categoria', 'fecha_publicación', 'modificado', 'user')

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()