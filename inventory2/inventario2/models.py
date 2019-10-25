from django.db import models

class Objeto(models.Model):
    ID = models.IntegerField()
    Marca = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=30)
    Estado = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=30)
    ID_Colegio = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Registro(models.Model):
    Fecha = models.DateField()
    Descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.Titulo

class Usuario(models.Model):
    ID = models.IntegerField()
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Laboratorio(models.Model):
    Ubicacion = models.IntegerField()
    Nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Conjunto(models.Model):
    ID = models.IntegerField()
    Nombre = models.CharField(max_length=30)
    Categoria = models.CharField(max_length=30)
    Stock = models.IntegerField()
    Descripcion = CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Armario(models.Model):
    ID = models.IntegerField()
    ID_Colegio = models.IntegerField()

    def __str__(self):
        return self.Nombre
