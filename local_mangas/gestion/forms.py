from django import forms
from .models import Mangas, Libros, Comics
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#forms para crear el registro:
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#forms para edición de perfil de usuarios:
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


#Formulario para mangas:
class MangasForm(forms.ModelForm):
    class Meta:
        model = Mangas
        fields = ['nombre', 'tomo', 'editorial', 'autor', 'demografia', 'cantidad_stock', 'cantidad_hojas', 'precio', 'imagen']

#Formulario para libros:
class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['nombre', 'autor', 'editorial', 'genero', 'cantidad_stock', 'cantidad_hojas', 'precio', 'imagen']

#Formulario para cómics:
class ComicsForm(forms.ModelForm):
    class Meta:
        model = Comics
        fields = ['nombre', 'editorial', 'autor', 'genero', 'cantidad_stock', 'cantidad_hojas', 'precio', 'imagen']
