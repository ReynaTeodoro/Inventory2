from django.contrib import admin
from .models import Objeto, Registro, Usuario, Laboratorio, Conjunto, Armario, Especialidad, Categoria
# Register your models here.



class RegistroAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', 'usuario')


class ConjuntoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'contar')

class ObjetoAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'

admin.site.register(Objeto, ObjetoAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Usuario)
admin.site.register(Laboratorio)
admin.site.register(Conjunto, ConjuntoAdmin)
admin.site.register(Armario)
admin.site.register(Especialidad)
admin.site.register(Categoria)
