from django import forms

class MangasForm(forms.Form):
    nombre = forms.CharField(max_length=150, required=True, label="Nombre del Manga")
    tomo = forms.IntegerField(required=True, label="Tomo del Manga")
    editorial = forms.CharField(max_length=150, required=True, label="Editorial del Manga")
    autor = forms.CharField(max_length=150, required=True, label="Autor del Manga")
    demografia = forms.CharField(max_length=150, required=True)
    cantidad_stock = forms.IntegerField(required=True, label="Cantidad en Stock")
    cantidad_hojas = forms.IntegerField(required=True, label="Cantidad de hojas")
    precio = forms.IntegerField(required=True, label="Precio")

class ComicsForm(forms.Form):
    nombre = forms.CharField(max_length=150, required=True, label="Nombre del Comic")
    editorial = forms.CharField(max_length=150, required=True, label="Editorial del Comic")
    autor = forms.CharField(max_length=150, required=True, label="Autor del Comic")
    genero = forms.CharField(max_length=150, required=True)
    cantidad_stock = forms.IntegerField(required=True, label="Cantidad en Stock")
    cantidad_hojas = forms.IntegerField(required=True, label="Cantidad de hojas")
    precio = forms.IntegerField(required=True, label="Precio")

class LibrosForm(forms.Form):
    nombre = forms.CharField(max_length=150, required=True, label="Nombre del Libro")
    editorial = forms.CharField(max_length=150, required=True, label="Editorial del Libro")
    autor = forms.CharField(max_length=150, required=True, label="Autor del Libro")
    genero = forms.CharField(max_length=150, required=True)
    cantidad_stock = forms.IntegerField(required=True, label="Cantidad en Stock")
    cantidad_hojas = forms.IntegerField(required=True, label="Cantidad de hojas")
    precio = forms.IntegerField(required=True, label="Precio")
