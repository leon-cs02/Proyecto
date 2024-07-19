from django.contrib import admin
from .models import *
# Register your models here.

class MangasAdmin(admin.ModelAdmin):
    list_display = ("nombre","tomo","editorial","autor","demografia","cantidad_hojas","cantidad_stock")

class LibrosAdmin(admin.ModelAdmin):
    list_display = ("nombre","editorial","autor","genero","cantidad_stock","cantidad_hojas")


admin.site.register(Mangas, MangasAdmin)
admin.site.register(Libros, LibrosAdmin)
