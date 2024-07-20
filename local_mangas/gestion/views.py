from django.shortcuts import render
from gestion.models import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView
from .forms import CustomUserProfileForm, ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile
from gestion.forms import *
from django.contrib.auth.decorators import login_required
from .models import Mangas, Libros, Comics
from django.conf import settings

# Métodos para visualizar en la página los html

def index(request):
    mangas = Mangas.objects.all()[:4]  # Traer los primeros 4 mangas
    libros = Libros.objects.all()[:4]  # Traer los primeros 4 libros
    comics = Comics.objects.all()[:4]  # Traer los primeros 4 cómics
    context = {
        'mangas': mangas,
        'libros': libros,
        'comics': comics,
        'MEDIA_URL': settings.MEDIA_URL,  # Agregar MEDIA_URL al contexto
    }
    return render(request, 'gestion/index.html', context)

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
    template_name = 'signup.html'

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes a los Mangas:

class MangasView(ListView, LoginRequiredMixin):
    model = Mangas

class MangasCreate(CreateView, LoginRequiredMixin):
    model = Mangas
    fields = ["nombre","tomo","editorial","autor","demografia","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("mangas")

class MangasUpdate(UpdateView, LoginRequiredMixin):
    model = Mangas
    fields = ["nombre","tomo","editorial","autor","demografia","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("mangas")

class MangasDelete(DeleteView, LoginRequiredMixin):
    model = Mangas
    success_url = reverse_lazy("mangas")

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes al Model Cómics:

class ComicsView(ListView, LoginRequiredMixin):
    model = Comics

class ComicsCreate(CreateView, LoginRequiredMixin):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("comics")

class ComicsUpdate(UpdateView, LoginRequiredMixin):
    model = Comics
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("comics")

class ComicsDelete(DeleteView, LoginRequiredMixin):
    model = Comics
    success_url = reverse_lazy("comics")

#------------------------------------------------------------------------------------------------------------

#Métodos pertenecientes al model Libros:

class LibrosView(ListView, LoginRequiredMixin):
    model = Libros

#Método para agregar a la BD:

class LibrosCreate(CreateView, LoginRequiredMixin):
    model = Libros
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("libros")

#Método para actualizar los campos de los libros:

class LibrosUpdate(UpdateView, LoginRequiredMixin):
    model = Libros
    fields = ["nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas","precio", "imagen"]
    success_url = reverse_lazy("libros")

#Método para borrar de la BD un libro:

class LibrosDelete(DeleteView, LoginRequiredMixin):
    model = Libros
    success_url = reverse_lazy("libros")


#------------------------------------------------------------------------------------------------------------

class FigurasView(ListView, LoginRequiredMixin):
    model = Figuras

class FigurasCreate(CreateView, LoginRequiredMixin):
    model = Figuras
    fields = ["nombre", "precio", "imagen"]
    success_url = reverse_lazy("figuras")

class FigurasUpdate(UpdateView, LoginRequiredMixin):
    model = Figuras
    fields = ["nombre", "precio", "imagen"]
    success_url = reverse_lazy("figuras")

class FigurasDelete(DeleteView, LoginRequiredMixin):
    model = Figuras
    success_url = reverse_lazy("figuras")

#------------------------------------------------------------------------------------------------------------

#Barra de búsqueda: 
from django.views.generic import ListView
from .models import Mangas, Libros, Comics

class SearchResultsView(ListView):
    template_name = 'gestion/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = {
            'mangas': Mangas.objects.filter(nombre__icontains=query),
            'libros': Libros.objects.filter(nombre__icontains=query),
            'comics': Comics.objects.filter(nombre__icontains=query)
        }
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset())
        context['query'] = self.request.GET.get('q')
        return context
#------------------------------------------------------------------------------------------------------------