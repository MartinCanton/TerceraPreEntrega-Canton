from django.db import models

class Libros(models.Model):
    titulo = models.CharField(max_length=100)
    escritor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.titulo} - {self.escritor} - {self.genero}"
    
class Musica(models.Model):
    cancion = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.cancion} - {self.artista} - {self.genero}"

class Peliculas(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.titulo} - {self.genero} - {self.director}"


