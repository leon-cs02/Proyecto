from django.urls import path, include
from gestion.views import *

urlpatterns = [
    #pagina principal
    path('', index, name="index"),
    path('mangas/', mangas, name="mangas"),
    path('comics/', comics, name="comics"),
    path('libros/', libros, name="libros"),
    path('usuarios/', usuarios, name="usuarios"),
    #Formularios
    path('mangasForm/', mangasForm, name="mangasForm"),
    path('comicsForm/', comicsForm, name="comicsForm"),
    path('librosForm/', librosForm, name="librosForm"),
    #Buscar
    path('buscarMangas/', buscarMangas, name="buscarMangas"),
    path('encontrarMangas/', encontrarMangas, name="encontrarMangas"),
    path('buscarComics/', buscarComics, name="buscarComics"),
    path('encontrarComics/', encontrarComics, name="encontrarComics"),
    path('buscarLibros/', buscarLibros, name="buscarLibros"),
    path('encontrarLibros/', encontrarLibros, name="encontrarLibros"),
]
