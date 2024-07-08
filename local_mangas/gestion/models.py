from django.db import models
# Modelo de gestion de stock

class Mangas(models.Model):
    nombre = models.CharField(max_length=150)
    tomo = models.IntegerField()
    editorial = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    demografia = models.CharField(max_length=150)
    cantidad_stock = models.IntegerField()
    cantidad_hojas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    #podemos crear la clase "Meta" para arreglar errores ortográficos u ordenar en qué orden ver los elementos con "ordering[]"

class Libros(models.Model):
    nombre = models.CharField(max_length=150)
    editorial = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    cantidad_stock = models.IntegerField()
    cantidad_hojas = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
class Comics(models.Model):
    nombre = models.CharField(max_length=150)
    editorial = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    cantidad_stock = models.IntegerField()
    cantidad_hojas = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_usuario}"
    
