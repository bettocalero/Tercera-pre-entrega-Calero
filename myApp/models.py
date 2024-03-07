from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length = 100)
    descriptcion = models.CharField(max_length = 100)
    fecha_estreno = models.DateField()

    def __str__(self) -> str:
        return self.nombre
    
class Libro(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 100)
    fecha_publicacion = models.DateField()

    def __str__(self) -> str:
        return self.nombre
    
class Serie(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    temporadas = models.IntegerField()
    cant_capitulos = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
