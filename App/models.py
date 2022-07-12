from django.db import models
# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=50) #perro, gato, etc.

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

