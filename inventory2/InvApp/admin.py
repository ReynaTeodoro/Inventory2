from django.contrib import admin
from .models import Objeto, Registro, Usuario, Laboratorio, Conjunto, Armario, Especialidad, Categoria
from django.contrib.admin.helpers import ActionForm
from django import forms


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', 'usuario')

def multiplicar_objeto(modeladmin, request, queryset):
    pass

class MultiplicarObjeto(ActionForm):
	price = forms.IntegerField()


class ObjetoAdmin(admin.ModelAdmin):
    action_form = MultiplicarObjeto
    actions = [multiplicar_objeto, ]

class ConjuntoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'contar')

admin.site.register(Objeto)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Usuario)
admin.site.register(Laboratorio)
admin.site.register(Conjunto, ConjuntoAdmin)
admin.site.register(Armario)
admin.site.register(Especialidad)
admin.site.register(Categoria)
