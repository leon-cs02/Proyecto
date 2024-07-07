from django.shortcuts import render
from gestion.models import *

# Create your views here.

def index(request):
    contexto = {
        
    }
    return render(request, 'cd_html/index.html', contexto)

def mangas(request):
    contexto = {
        "mangas": Mangas.objects.all()
    }
    return render(request, 'cd_html/mangas.html', contexto)

def libros(request):
    contexto = {
        "libros": Libros.objects.all()
    }
    return render(request, 'cd_html/libros.html', contexto)

def usuarios(request):
    contexto = {
        "usuarios": Usuarios.objects.all()
    }
    return render(request, 'cd_html/usuarios.html', contexto)