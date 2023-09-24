from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('libro/', ver_libros, name="VerLibros"),
    path('musica/', ver_musica, name="VerMusica"),
    path('peliculas/', ver_peliculas, name="VerPeliculas"),
    path('librosformulario/', libros_formulario, name="LibrosFormularios"),
    path('musicaformulario', musica_formulario, name="MusicaFormularios" ),
    path('pelisformulario/', pelis_formulario, name="PelisFormularios"),
    path('busquedagenero/', busqueda_genero, name="BuscarGenero"),
    path('resultado/', resultado, name="ResultadosBusqueda")

   
    ]