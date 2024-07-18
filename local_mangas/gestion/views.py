from django.shortcuts import render
from gestion.models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, FormView, UpdateView

# Métodos para visualizar en la página los html

from gestion.forms import *



def index(request):
    contexto = {
        
    }
    return render(request, 'gestion/index.html', contexto)


#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes a los Mangas:

def mangas(request):
    contexto = {
        "mangas": Mangas.objects.all()
    }
    return render(request, 'gestion/mangas.html', contexto)

#Form del Manga

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
            form_precio = miForm.cleaned_data.get("precio")
            mangas = Mangas(nombre=form_nombre, tomo=form_tomo, editorial=form_editorial, autor=form_autor, demografia=form_demografia, cantidad_stock=form_cantidad_stock, cantidad_hojas = form_cantidad_hojas, precio = form_precio)
            mangas.save()
            contexto = {"mangas": Mangas.objects.all()}
            return render(request,"gestion/mangas.html", contexto)
    else:
        miForm = MangasForm()
    return render(request, "gestion/mangasForm.html", {"form": miForm})

#Buscar y encontrar del Manga:

def buscarMangas(request):
    return render(request, "gestion/buscarMangas.html")

def encontrarMangas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        mangas = Mangas.objects.filter(nombre__icontains=patron)
        contexto = {"mangas": mangas}
    else:
        contexto = {"mangas": Mangas.objects.all()}
    return render(request, "gestion/mangas.html", contexto)

#Modificar Mangas

def mangasMod(request, id_mangas):
    mangas = Mangas.objects.get(id=id_mangas)
    if request.method == "POST":
        miForm = MangasForm(request.POST)
        if miForm.is_valid():
            mangas.nombre = miForm.cleaned_data.get("nombre")
            mangas.tomo = miForm.cleaned_data.get("tomo")
            mangas.editorial = miForm.cleaned_data.get("editorial")
            mangas.autor = miForm.cleaned_data.get("autor")
            mangas.demografia = miForm.cleaned_data.get("demografia")
            mangas.cantidad_stock = miForm.cleaned_data.get("cantidad_stock")
            mangas.cantidad_hojas = miForm.cleaned_data.get("cantidad_hojas")
            mangas.precio = miForm.cleaned_data.get("precio")
            mangas.save()
            contexto = {"mangas": Mangas.objects.all()}
            return render(request,"gestion/mangas.html", contexto)
    else:
        miForm = MangasForm(initial={"nombre": mangas.nombre, 
                                     "tomo": mangas.tomo , 
                                     "editorial": mangas.editorial, 
                                     "autor": mangas.autor, 
                                     "demografia": mangas.demografia, 
                                     "cantidad_stock": mangas.cantidad_stock,
                                     "cantidad_hojas": mangas.cantidad_hojas,
                                     "precio": mangas.precio})
        
    return render(request, "gestion/mangasForm.html", {"form": miForm})

#Borrar Mangas:

def mangasDel(request, id_mangas):
    mangas = Mangas.objects.get(id=id_mangas)
    mangas.delete()
    contexto = {"mangas": Mangas.objects.all()}
    return render(request,"gestion/mangas.html", contexto)

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes al Model Cómics:

class ComicsView(ListView):
    model = Comics

class ComicsCreate(CreateView):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio"]
    success_url = reverse_lazy("comics")

class ComicsUpdate(UpdateView):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio"]
    success_url = reverse_lazy("comics")

class ComicsDelete(DeleteView):
    model = Comics
    success_url = reverse_lazy("comics")

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes al model Libros:

def libros(request):
    contexto = {
        "libros": Libros.objects.all()
    }
    return render(request, 'gestion/libros.html', contexto)

#Form de los Libros:

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
            form_precio = miForm.cleaned_data.get("precio")
            libros = Libros(nombre=form_nombre, editorial=form_editorial, autor=form_autor, genero=form_genero, cantidad_stock=form_cantidad_stock, cantidad_hojas = form_cantidad_hojas, precio = form_precio)
            libros.save()
            contexto = {"libros": Libros.objects.all()}
            return render(request,"gestion/libros.html", contexto)
    else:
        miForm = LibrosForm()
    return render(request, "gestion/librosForm.html", {"form": miForm})

#Buscar y encontrar los Libros:

def buscarLibros(request):
    return render(request, "gestion/buscarLibros.html")

def encontrarLibros(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libros = Libros.objects.filter(nombre__icontains=patron)
        contexto = {"libros": libros}
    else:
        contexto = {"libros": Libros.objects.all()}
    return render(request, "gestion/libros.html", contexto)

#Modificar Libros:

def librosMod(request, id_libros):
    libros = Libros.objects.get(id=id_libros)
    if request.method == "POST":
        miForm = LibrosForm(request.POST)
        if miForm.is_valid():
            libros.nombre = miForm.cleaned_data.get("nombre")
            libros.editorial = miForm.cleaned_data.get("editorial")
            libros.autor = miForm.cleaned_data.get("autor")
            libros.genero = miForm.cleaned_data.get("genero")
            libros.cantidad_stock = miForm.cleaned_data.get("cantidad_stock")
            libros.cantidad_hojas = miForm.cleaned_data.get("cantidad_hojas")
            libros.precio = miForm.cleaned_data.get("precio")
            libros.save()
            contexto = {"libros": Libros.objects.all()}
            return render(request,"cd_html/libros.html", contexto)
    else:
        miForm = LibrosForm(initial={"nombre": libros.nombre,  
                                     "editorial": libros.editorial, 
                                     "autor": libros.autor, 
                                     "genero": libros.genero, 
                                     "cantidad_stock": libros.cantidad_stock,
                                     "cantidad_hojas": libros.cantidad_hojas,
                                     "precio": libros.precio})
        
    return render(request, "gestion/librosForm.html", {"form": miForm})

#Borrar Libros:

def librosDel(request, id_libros):
    libros = Libros.objects.get(id=id_libros)
    libros.delete()
    contexto = {"libros": Libros.objects.all()}
    return render(request,"gestion/libros.html", contexto)


#------------------------------------------------------------------------------------------------------------

#Métodos relacionados con el Model Usuarios:

def usuarios(request):
    contexto = {
        "usuarios": Usuarios.objects.all()
    }
    return render(request, 'gestion/usuarios.html', contexto)
