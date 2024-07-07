from django.urls import path, include
from gestion.views import *

urlpatterns = [
    path('', index, name="index"),
    path('mangas/', mangas, name="mangas"),
    path('libros/', libros, name="libros"),
    path('usuarios/', usuarios, name="usuarios"),
]
