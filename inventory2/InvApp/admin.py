from django.contrib import admin
from .models import Objeto, Registro, Usuario, Laboratorio, Conjunto, Armario, Especialidad, Categoria
from django.contrib.admin.helpers import ActionForm
from django import forms
import datetime
from django.shortcuts import redirect

def redirect_pdf(modeladmin, request, queryset):
    return redirect("http://127.0.0.1:8000/registro")

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', Usuario)
    actions = [redirect_pdf]

def multiplicar_objeto(modeladmin, request, queryset):
    veces = request.POST.get('veces')
    for i in range(int(veces)):
        for object in queryset:
            object.id = None
            object.save()

class MultiplicarObjeto(ActionForm):
	veces = forms.IntegerField()



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
            objeto.delete()


    actions = [eliminarObjeto, multiplicar_objeto]
    action_form = MultiplicarObjeto

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        timestr = datetime.datetime.now()
        descripcion = ("Se añadio el objeto: " + obj.modelo + ", " +obj.marca)

        Registro.objects.create(fecha=timestr, descripcion= descripcion)

admin.site.register(Objeto, ObjetoAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Usuario)
admin.site.register(Laboratorio)
admin.site.register(Conjunto, ConjuntoAdmin)
admin.site.register(Armario)
admin.site.register(Especialidad)
admin.site.register(Categoria)
