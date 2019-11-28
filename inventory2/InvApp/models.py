from django.db import models
from django import forms
from django.db.models import Count
from django.contrib.admin.helpers import ActionForm
import datetime

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Conjunto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def contar(self):
        import re
        conjunto = Conjunto.objects.annotate(Count('objeto'))
        valConjunto = conjunto.filter(nombre=self.nombre).values_list('objeto__count')
        strConjunto = re.findall('\d+', str(valConjunto))
        return strConjunto

    def __str__(self):
        return self.nombre


class MultiplicarObjeto(ActionForm):
	price = forms.IntegerField()

class Objeto(models.Model):
    action_form = MultiplicarObjeto
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    estado = [
    (1, "Disponible"),
    (2, "Prestado"),
    (3, "En mantenimiento")
    ]
    estado = models.IntegerField(choices=estado,default=1)
    condicion = [
    (1, "Nuevo"),
    (2, "Usado"),
    (3, "Arreglar"),
    (4, "Roto")
    ]
    condicion = models.IntegerField(choices=condicion,default=1)
    descripcion = models.CharField(max_length=30)
    id_Colegio = models.CharField(max_length=30)

    armario = models.ForeignKey('Armario', on_delete=models.CASCADE)
    conjunto = models.ForeignKey('Conjunto', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo

class Registro(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)

    def __str__(self):
        return str(self.fecha)

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)

    def __str__(self):
        return self.nombre

class Laboratorio(models.Model):
    ubicacion = models.IntegerField()
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    def registrarObjeto(arg):
        pass

    def agregar(arg):
        pass

    def quitar(arg):
        pass

    def moverObjeto(arg):
        pass



class Armario(models.Model):
    nombre = models.CharField(max_length=30,default='1')
    id_Colegio = models.IntegerField()
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Especialidad(models.Model):

    class Meta:
        verbose_name_plural = 'Especialidades'

    materia = models.CharField(max_length=30)

    def __str__(self):
        return self.materia
