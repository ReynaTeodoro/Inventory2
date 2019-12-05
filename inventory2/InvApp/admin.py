from django.contrib import admin
from .models import Objeto, Registro, Laboratorio, Conjunto, Armario, Especialidad, Categoria
from django.contrib.admin.helpers import ActionForm
from django import forms
import datetime
from django.shortcuts import redirect
from .views import *
import re


class ArmarioInline(admin.TabularInline):
    model = Armario

class ObjetoInline(admin.TabularInline):
    model = Objeto


class RegistroAdmin(admin.ModelAdmin):
    change_list_template = 'change_list2.html'
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
    change_list_template = 'change_list2.html'
    list_display = ('nombre', 'descripcion', 'categoria', 'contar')
    list_filter = ('nombre',  'categoria' ,)
    search_fields = ['nombre', 'categoria__nombre',]
    inlines=[ObjetoInline,]

class ObjetoAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'
    list_filter = ('marca',  'condicion' , 'estado', )

    search_fields = ['marca','modelo','descripcion','id_Colegio','armario__nombre', 'conjunto__nombre', 'categoria__nombre','armario__laboratorio__nombre']
    list_display = ('marca', 'modelo', 'estado', 'condicion', 'descripcion', 'id_Colegio','armario', 'conjunto', 'categoria','get_armarioLab')

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
#                print(str(int(numeros[0])+1))
#                print(letras)
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

class LaboratorioAdmin(admin.ModelAdmin):
    change_list_template = 'change_list2.html'
    list_display = ('nombre', 'ubicacion',)
    list_filter = ('nombre', 'ubicacion',)
    search_fields = ['nombre','ubicacion']
    inlines=[ArmarioInline,]

class EspecialidadAdmin(admin.ModelAdmin):
    change_list_template = 'change_list2.html'
    list_display = ('materia',)
    list_filter = ('materia',)
    search_fields = ['materia']


class CategoriaAdmin(admin.ModelAdmin):
    change_list_template = 'change_list2.html'
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ['nombre']

class ArmarioAdmin(admin.ModelAdmin):
    change_list_template = 'change_list2.html'
    list_display = ('nombre', 'laboratorio',)
    list_filter = ('nombre', 'laboratorio',)
    search_fields = ['nombre', 'laboratorio__nombre']

admin.site.register(Objeto, ObjetoAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Conjunto, ConjuntoAdmin)
admin.site.register(Armario, ArmarioAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Categoria, CategoriaAdmin)
