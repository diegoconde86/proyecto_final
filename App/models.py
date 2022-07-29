from tkinter import image_names
from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=50) #perro, gato, etc.
    autor = models.CharField(max_length=40,null=True)
    fecha = models.DateTimeField(null=True)
    imagen = models.ImageField(upload_to = "mascotas", null=True, blank=True)

    #titulo, subtitulo, cuerpo, autor, imagenes, fecha

    def __str__(self) -> str:
        return 'nombre: '+self.nombre + ' edad: ' + str(self.edad) + ' tipo: ' + self.tipo

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return 'nombre: '+self.nombre + ' apellido: ' + self.apellido + ' email: ' + self.email

class Veterinario(models.Model):
    nombre =models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 'nombre: '+self.nombre + ' especialidad: ' + self.especialidad

class Articulo (models.Model):  #Clase para importar articulos de Veterinaria
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = RichTextField(blank=True, null=True)
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField()
    editado = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to = "articulos", null=True, blank=True)