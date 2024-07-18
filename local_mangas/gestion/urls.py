from django.urls import path, include
from gestion.views import *

urlpatterns = [
    #pagina principal
    path('', index, name="index"),
    path('usuarios/', usuarios, name="usuarios"),

    #Mangas:

    path('mangas/', mangas, name="mangas"),
    path('mangasForm/', mangasForm, name="mangasForm"),
    path('buscarMangas/', buscarMangas, name="buscarMangas"),
    path('encontrarMangas/', encontrarMangas, name="encontrarMangas"),
    path('mangasMod/<id_mangas>/', mangasMod, name="mangasMod"),
    path('mangasDel/<id_mangas>/', mangasDel, name="mangasDel"),

    #Libros:

    path('libros/', libros, name="libros"),
    path('librosForm/', librosForm, name="librosForm"),
    path('buscarLibros/', buscarLibros, name="buscarLibros"),
    path('encontrarLibros/', encontrarLibros, name="encontrarLibros"),
    path('librosMod/<id_libros>/', librosMod, name="librosMod"),
    path('librosDel/<id_libros>/', librosDel, name="librosDel"),

    #Comics:
    path('comics/', ComicsView.as_view(), name="comics"),
    path('comicsCreate/', ComicsCreate.as_view(), name="comicsCreate"),
    path('comicsUpdate/<int:pk>/', ComicsUpdate.as_view(), name="comicsUpdate"),
    path('comicsDelete/<int:pk>/', ComicsDelete.as_view(), name="comicsDelete"),

]
