from django.shortcuts import render
from gestion.models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, FormView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView


# Métodos para visualizar en la página los html

from gestion.forms import *



def index(request):
    contexto = {
        
    }
    return render(request, 'gestion/index.html', contexto)

#------------------------------------------------------------------------------------------------------------

class CustomLoginView(LoginView):
    template_name = 'login.html'

#Utilizo CBV para modificar el perfil de usuario, validar los métodos get y post, guardar los datos y finalizar
#con un mensaje que indique que su perfil fue modificado:

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        return self.render_to_response({'u_form': u_form, 'p_form': p_form})

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Se guardaron los datos con éxito!')
            return redirect('profile')

        return self.render_to_response({'u_form': u_form, 'p_form': p_form})
    
#Registro:

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirige a la página de login después de registrarse
    template_name = 'gestion/login.html'

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes a los Mangas:

class MangasView(ListView):
    model = Mangas

class MangasCreate(CreateView):
    model = Mangas
    fields = ["nombre","tomo","editorial","autor","demografia","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("mangas")

class MangasUpdate(UpdateView):
    model = Mangas
    fields = ["nombre","tomo","editorial","autor","demografia","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("mangas")

class MangasDelete(DeleteView):
    model = Mangas
    success_url = reverse_lazy("mangas")

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes al Model Cómics:

class ComicsView(ListView):
    model = Comics

class ComicsCreate(CreateView):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("comics")

class ComicsUpdate(UpdateView):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
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
            form_imagen = miForm.cleaned_data.get("imagen")
            libros = Libros(nombre=form_nombre, editorial=form_editorial, autor=form_autor, genero=form_genero, cantidad_stock=form_cantidad_stock, cantidad_hojas = form_cantidad_hojas, precio = form_precio, imagen = form_imagen)
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
            libros.imagen = miForm.cleaned_data.get("imagen")
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
                                     "precio": libros.precio,
                                     "imagen": libros.imagen})
        
    return render(request, "gestion/librosForm.html", {"form": miForm})

#Borrar Libros:

def librosDel(request, id_libros):
    libros = Libros.objects.get(id=id_libros)
    libros.delete()
    contexto = {"libros": Libros.objects.all()}
    return render(request,"gestion/libros.html", contexto)


#------------------------------------------------------------------------------------------------------------

