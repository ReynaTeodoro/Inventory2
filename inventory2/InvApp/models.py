from django.db import models

# Create your models here.
from django.db import models

class Objeto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    id_Colegio = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Registro(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.Titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)

    def __str__(self):
        return self.Nombre

class Laboratorio(models.Model):
    ubicacion = models.IntegerField()
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Conjunto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Armario(models.Model):
    id_Colegio = models.IntegerField()

    def __str__(self):
        return self.Nombre

class Especialidad(models.Model):
    materia = models.CharField(max_length=30)

    def __str__(self):
        return self.materia
