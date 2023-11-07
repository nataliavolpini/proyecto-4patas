from django.db import models

# Create your models here.

class Perro(models.Model):

    nombre = models.CharField(max_length=64)
    raza =  models.CharField(max_length=64, blank=True)  
    fecha_nacimiento = models.DateField(null=True)
    descripcion = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.nombre} ({self.raza})'
    
class Gato(models.Model):

    nombre = models.CharField(max_length=64)
    color =  models.CharField(max_length=64)  
    fecha_nacimiento = models.DateField(null=True) 
    descripcion = models.CharField(max_length=256)  

    def __str__(self):
        return f'{self.nombre} ({self.color})' 

class Caballo(models.Model):

    nombre = models.CharField(max_length=64)
    color =  models.CharField(max_length=64)  
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f'{self.nombre} ({self.color})'     
