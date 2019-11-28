from django.contrib import admin
from .models import Objeto, Registro, Usuario, Laboratorio, Conjunto, Armario, Especialidad, Categoria
from django.contrib.admin.helpers import ActionForm
from django import forms
import datetime
from django.shortcuts import redirect

def redirect_pdf(modeladmin, request, queryset):
    return redirect("http://127.0.0.1:8000")

class RegistroAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('fecha', 'descripcion', Usuario)
    actions = [redirect_pdf]
=======
    list_display = ('fecha', 'descripcion', 'usuario')
    list_filter = ('usuario', 'fecha',)
    search_fields = ['usuario','fecha', 'descripcion']
>>>>>>> filters

def multiplicar_objeto(modeladmin, request, queryset):
    veces = request.POST.get('veces')
    for i in range(int(veces)):
        for object in queryset:
            object.id = None
            object.save()

class MultiplicarObjeto(ActionForm):
	veces = forms.IntegerField()



class ConjuntoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria',)
    list_filter = ('nombre',  'categoria' ,)
    search_fields = ['nombre', 'categoria__nombre',]


class ObjetoAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'
    list_filter = ('marca',  'modelo' , 'estado', )
    search_fields = ['modelo', 'marca', 'estado', 'condicion', 'descripcion','id_Colegio', 'armario', 'conjunto', 'categoria']

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

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','mail',)
    list_filter = ('nombre','apellido',)
    search_fields = ['nombre','apellido','mail']

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion',)
    list_filter = ('nombre', 'ubicacion',)
    search_fields = ['nombre','ubicacion']

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('materia',)
    list_filter = ('materia',)
    search_fields = ['materia']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ['nombre']

class ArmarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_Colegio', 'laboratorio',)
    list_filter = ('nombre', 'id_Colegio', 'laboratorio',)
    search_fields = ['nombre', 'id_Colegio', 'laboratorio__nombre']

admin.site.register(Objeto, ObjetoAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Conjunto, ConjuntoAdmin)
admin.site.register(Armario, ArmarioAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Categoria, CategoriaAdmin)
