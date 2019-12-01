from django.contrib import admin
from .models import Objeto, Registro, Usuario, Laboratorio, Conjunto, Armario, Especialidad, Categoria
from django.contrib.admin.helpers import ActionForm
from django import forms
import datetime
from django.shortcuts import redirect
from .views import *
import re

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', 'usuario')
    list_filter = ('usuario', 'fecha',)
    search_fields = ['usuario','fecha', 'descripcion']

    def redirect_pdf(modeladmin, request, queryset):
        return registroPdf(request, queryset=queryset)
    redirect_pdf.short_description = "Imprimir registro(s)"

    actions = [redirect_pdf]

class MultiplicarObjeto(ActionForm):
	veces = forms.IntegerField()


class ConjuntoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria', 'contar')
    list_filter = ('nombre',  'categoria' ,)
    search_fields = ['nombre', 'categoria__nombre',]

class ObjetoAdmin(admin.ModelAdmin):
    
    change_list_template = 'change_list.html'
    list_filter = ('marca',  'modelo' , 'estado', )
    list_display = ('marca', 'modelo', 'estado', 'condicion', 'descripcion', 'id_Colegio','armario', 'conjunto', 'categoria', )
    search_fields = ['modelo', 'marca', 'estado', 'condicion', 'descripcion','id_Colegio', 'armario', 'conjunto', 'categoria']


    def objeto_pdf(modeladmin, request, queryset):
        return objetoPdf(request, queryset)
    objeto_pdf.short_description = "Imprimir objeto(s)"

    def multiplicar_objeto(modeladmin, request, queryset):
        veces = request.POST.get('veces')
        print(veces)
        for i in range(int(veces)):
            for object in queryset:
                id_cole = (object.id_Colegio)
                numeros = re.findall(r'\d+', str(id_cole))
                letras = re.findall("[a-zA-Z]+", str(id_cole))
                print(str(int(numeros[0])+1))
                print(letras)
                if not letras:
                    object.id_Colegio = str(int(numeros[0])+1)
                else:
                    object.id_Colegio = str(letras[0])+str(int(numeros[0])+1)
                object.id = None
                object.save()
    multiplicar_objeto.short_description = "Multiplicar objeto(s)"


    def changelist_view(self, request):
        extra_context = {
            'armarios': Armario.objects.all(),
            'objetos': Objeto.objects.all()
        }
        return super(ObjetoAdmin, self).changelist_view(request, extra_context=extra_context)

    def eliminarObjeto(modeladmin, request, queryset):
        for objeto in queryset:
            objeto.delete()
            timestr = datetime.datetime.now()
            descripcion = ("Se borro el objeto: " +  objeto.id_Colegio)
            user_name = None
            user_name = request.user.get_username()
            Registro.objects.create(fecha=timestr,descripcion=descripcion, usuario=user_name)
    eliminarObjeto.short_description = "Borrar objeto(s) y registrarlo(s)"
    action_form = MultiplicarObjeto

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        timestr = datetime.datetime.now()
        descripcion = ("Se añadio el objeto: " + obj.modelo + ", " +obj.marca)

        Registro.objects.create(fecha=timestr, descripcion= descripcion)

    def mover(modeladmin, request, queryset):
        new_armario = request.POST.get('veces')
        for objeto in queryset:
            print(objeto.estado)
            if (objeto.estado != 3):
                timestr = datetime.datetime.now()
                descripcion = ("Se movio el objeto: " + objeto.modelo + ", " + objeto.marca + ' del armario: ' + objeto.armario.nombre + ' al armario ' + Armario.objects.get(id=new_armario).nombre)
                user_name = request.user.get_username()
                Registro.objects.create(fecha=timestr,descripcion=descripcion, usuario=user_name)
                objeto.armario = Armario.objects.get(id=new_armario)
                objeto.save()

    actions = [eliminarObjeto, multiplicar_objeto, mover, objeto_pdf]
    action_form = MultiplicarObjeto
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
