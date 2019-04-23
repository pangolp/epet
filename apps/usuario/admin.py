from django.contrib import admin

from .models import Sexo, Documento, Pais, Perfil


@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
	list_display = ('tipo',)


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
	list_display = ('user', 'segundo_apellido', 'segundo_nombre', 'sexo', 'tipo_documento', 'numero_documento', 'numero_empleado', 'legajo_cpe', 'observación', 'pais_nacimiento', 'fecha_ingreso', 'fecha_egreso')
