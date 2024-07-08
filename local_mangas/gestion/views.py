from django.shortcuts import render
from gestion.models import *

# Métodos para visualizar en la página los html

from gestion.forms import *

def index(request):
    contexto = {
        
    }
    return render(request, 'cd_html/index.html', contexto)

def mangas(request):
    contexto = {
        "mangas": Mangas.objects.all()
    }
    return render(request, 'cd_html/mangas.html', contexto)

def comics(request):
    contexto = {
        "comics": Comics.objects.all()
    }
    return render(request, 'cd_html/comics.html', contexto)

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

#Formularios

def mangasForm(request):
    if request.method == "POST":
        miForm = MangasForm(request.POST)
        if miForm.is_valid():
            form_nombre = miForm.cleaned_data.get("nombre")
            form_tomo = miForm.cleaned_data.get("tomo")
            form_editorial = miForm.cleaned_data.get("editorial")
            form_autor = miForm.cleaned_data.get("autor")
            form_demografia = miForm.cleaned_data.get("demografia")
            form_cantidad_stock = miForm.cleaned_data.get("cantidad_stock")
            form_cantidad_hojas = miForm.cleaned_data.get("cantidad_hojas")
            mangas = Mangas(nombre=form_nombre, tomo=form_tomo, editorial=form_editorial, autor=form_autor, demografia=form_demografia, cantidad_stock=form_cantidad_stock, cantidad_hojas = form_cantidad_hojas)
            mangas.save()
            contexto = {"mangas": Mangas.objects.all()}
            return render(request,"cd_html/mangas.html", contexto)
    else:
        miForm = MangasForm()
    return render(request, "cd_html/mangasForm.html", {"form": miForm})
    
def comicsForm(request):
    if request.method == "POST":
        miForm = ComicsForm(request.POST)
        if miForm.is_valid():
            form_nombre = miForm.cleaned_data.get("nombre")
            form_editorial = miForm.cleaned_data.get("editorial")
            form_autor = miForm.cleaned_data.get("autor")
            form_genero = miForm.cleaned_data.get("genero")
            form_cantidad_stock = miForm.cleaned_data.get("cantidad_stock")
            form_cantidad_hojas = miForm.cleaned_data.get("cantidad_hojas")
            comics = Comics(nombre=form_nombre, editorial=form_editorial, autor=form_autor, genero=form_genero, cantidad_stock=form_cantidad_stock, cantidad_hojas = form_cantidad_hojas)
            comics.save()
            contexto = {"comics": Comics.objects.all()}
            return render(request,"cd_html/comics.html", contexto)
    else:
        miForm = ComicsForm()
    return render(request, "cd_html/comicsForm.html", {"form": miForm})
    
def librosForm(request):
    if request.method == "POST":
        miForm = LibrosForm(request.POST)
        if miForm.is_valid():
            form_nombre = miForm.cleaned_data.get("nombre")
            form_editorial = miForm.cleaned_data.get("editorial")
            form_autor = miForm.cleaned_data.get("autor")
            form_genero = miForm.cleaned_data.get("genero")
            form_cantidad_stock = miForm.cleaned_data.get("cantidad_stock")
            form_cantidad_hojas = miForm.cleaned_data.get("cantidad_hojas")
            libros = Libros(nombre=form_nombre, editorial=form_editorial, autor=form_autor, genero=form_genero, cantidad_stock=form_cantidad_stock, cantidad_hojas = form_cantidad_hojas)
            libros.save()
            contexto = {"libros": Libros.objects.all()}
            return render(request,"cd_html/libros.html", contexto)
    else:
        miForm = LibrosForm()
    return render(request, "cd_html/librosForm.html", {"form": miForm})

#Métodos para buscar en cada model

#Métodos para encontrar Mangas:

def buscarMangas(request):
    return render(request, "cd_html/buscarMangas.html")

def encontrarMangas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        mangas = Mangas.objects.filter(nombre__icontains=patron)
        contexto = {"mangas": mangas}
    else:
        contexto = {"mangas": Mangas.objects.all()}
    return render(request, "cd_html/mangas.html", contexto)

#Métodos para encontrar Comics:

def buscarComics(request):
    return render(request, "cd_html/buscarComics.html")

def encontrarComics(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        comics = Comics.objects.filter(nombre__icontains=patron)
        contexto = {"comics": comics}
    else:
        contexto = {"comics": Comics.objects.all()}
    return render(request, "cd_html/comics.html", contexto)

#Métodos para encontrar Libros:

def buscarLibros(request):
    return render(request, "cd_html/buscarLibros.html")

def encontrarLibros(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libros = Libros.objects.filter(nombre__icontains=patron)
        contexto = {"libros": libros}
    else:
        contexto = {"comics": Libros.objects.all()}
    return render(request, "cd_html/libros.html", contexto)