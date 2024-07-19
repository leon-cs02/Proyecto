from django.urls import path, include
from gestion.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    #pagina principal
    path('', index, name="index"),

    #Mangas:

    path('mangas/', MangasView.as_view(), name="mangas"),
    path('mangasCreate/', MangasCreate.as_view(), name="mangasCreate"),
    path('mangasUpdate/<int:pk>/', MangasUpdate.as_view(), name="mangasUpdate"),
    path('mangasDelete/<int:pk>/', MangasDelete.as_view(), name="mangasDelete"),

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

    #Autentication:
    path('login/', auth_views.LoginView.as_view(template_name='gestion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
