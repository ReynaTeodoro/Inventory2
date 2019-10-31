from django.db import models

# Create your models here.
from django.db import models

class Conjunto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Objeto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    id_Colegio = models.CharField(max_length=30)

    armario = models.ForeignKey('Armario', on_delete=models.CASCADE)
    conjunto = models.ForeignKey('Conjunto', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)


    def __str__(self):
        return self.Nombre

class Registro(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=30)

    conjuntos = models.ManyToManyField(Conjunto)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

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

    def registrarObjeto(arg):
        pass

    def agregar(arg):
        pass

    def quitar(arg):
        pass

    def moverObjeto(arg):
        pass



class Armario(models.Model):
    id_Colegio = models.IntegerField()

    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Especialidad(models.Model):
    materia = models.CharField(max_length=30)

    def __str__(self):
        return self.materia

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
