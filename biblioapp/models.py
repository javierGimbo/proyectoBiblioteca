from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Usuario(AbstractUser):
    dni= models.TextField(max_length=10)
    direccion= models.TextField()
    telefono= models.IntegerField()


    def __str__(self):
        return self.dni



class Libro(models.Model):
    titulo= models.TextField(max_length=200)
    autores= models.ManyToManyField("Autor")
    editorial= models.ForeignKey("Editorial", on_delete=models.CASCADE)
    fechaPublicacion= models.DateField()
    genero= models.CharField()
    isbn= models.IntegerField()
    resumen= models.TextField()
    portada= models.ImageField(upload_to='portadas/', null=True, blank=True)

    disponibilidad_choices =(
        ('disponible', 'Disponible'),
        ('prestamo', 'Prestamo'),
    )

    disponibilidad= models.CharField(max_length=20, choices=disponibilidad_choices, default='disponible')

    def __str__(self):
        return self.titulo
    
class Autor(models.Model):
    nombre= models.TextField(max_length=100)
    biografia= models.TextField()
    foto= models.ImageField(upload_to='autores/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    

class Prestamo(models.Model):
    libro=models.ForeignKey("Libro", on_delete=models.CASCADE)
    fechaPrestamo=models.DateField()
    fechaDevolucion=models.DateField()
    usuario=models.ForeignKey("Usuario", on_delete=models.CASCADE)

    estado_choices =(
        ('prestado', 'Prestado'),
        ('devuelto', 'Devuelto'),
    )

    estado= models.CharField(max_length=20, choices=estado_choices)

    
    def __str__(self):
        return self.titulo
    

class Editorial(models.Model):
    nombre= models.CharField(max_length=100)
    direccion= models.TextField()
    sitioWeb= models.URLField()

    def __str__(self):
        return self.nombre