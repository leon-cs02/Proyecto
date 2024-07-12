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
    #Actualizar:
    path('mangasMod/<id_mangas>/', mangasMod, name="mangasMod"),
    path('comicsMod/<id_comics>/', comicsMod, name="comicsMod"),
    path('librosMod/<id_libros>/', librosMod, name="librosMod"),
    #Borrar:
    path('mangasDel/<id_mangas>/', mangasDel, name="mangasDel"),
    path('comicsDel/<id_comics>/', comicsDel, name="comicsDel"),
    path('librosDel/<id_libros>/', librosDel, name="librosDel"),
]
