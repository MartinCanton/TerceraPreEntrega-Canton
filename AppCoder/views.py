from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ver_libros(request):
    return render(request, "AppCoder/ver_libros.html")

def ver_musica(request):
    return render(request, "AppCoder/ver_musica.html")

def ver_peliculas(request):
    return render(request, "AppCoder/ver_peliculas.html")

def libros_formulario(request):
      
    if request.method == "POST":
        formulario1 = Libro_Formulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            libro = Libros(titulo=info["titulo"], escritor=info["escritor"], genero=info["genero"])
            libro.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = Libro_Formulario()
        return render(request, "AppCoder/libros_formulario.html", {"form1" : formulario1})

def musica_formulario(request):
      
    if request.method == "POST":
        formulario1 = Musica_Formulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            musica = Musica(cancion=info["cancion"], artista=info["artista"], genero=info["genero"])
            musica.save()
        return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = Musica_Formulario()
        return render(request, "AppCoder/musica_formulario.html", {"form1" : formulario1})

def pelis_formulario(request):
      
    if request.method == "POST":
        formulario1 = Peliculas_Formulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            pelis = Peliculas(titulo=info["titulo"], director=info["director"], genero=info["genero"])
            pelis.save()
        return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = Peliculas_Formulario()
        return render(request, "AppCoder/pelis_formulario.html", {"form1" : formulario1})

def busqueda_genero(request):
    return render(request, "AppCoder/inicio.html")

def resultado(request):

    if request.GET["genero"]:
        genero=request.GET["genero"]
        libros = Libros.objects.filter(genero__icontains=genero)
        return render(request, "AppCoder/inicio.html", {"libros":libros, "genero":genero})
    else:
        return render(request, "AppCoder/inicio.html")






