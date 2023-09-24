from django import forms

class Libro_Formulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    escritor = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    
class Peliculas_Formulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    director = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    
class Musica_Formulario(forms.Form):
    cancion = forms.CharField(max_length=200)
    artista = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)

