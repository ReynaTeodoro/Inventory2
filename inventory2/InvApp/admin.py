from django.contrib import admin
from .models import Objeto, Registro, Usuario, Laboratorio, Conjunto, Armario, Especialidad, Categoria
# Register your models here.
import datetime
 #listener


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', Usuario)

class ConjuntoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'contar')

class ObjetoAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'

    def changelist_view(self, request):
        extra_context = {
            'labs': Laboratorio.objects.all(),
            'objetos': Objeto.objects.all()
        }
        return super(ObjetoAdmin, self).changelist_view(request, extra_context=extra_context)

    def eliminarObjeto(modeladmin, request, queryset):
        for objeto in queryset:
            objeto.borrarObjeto()

    actions = [eliminarObjeto,]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        timestr = datetime.datetime.now()
        descripcion = ("Se añadio el objeto: " + obj.modelo + ", " +obj.marca)

        Registro.objects.create(fecha=timestr, descripcion= descripcion)

admin.site.register(Objeto,ObjetoAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Usuario)
admin.site.register(Laboratorio)
admin.site.register(Conjunto, ConjuntoAdmin)
admin.site.register(Armario)
admin.site.register(Especialidad)
admin.site.register(Categoria)
