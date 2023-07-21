from django.db import models


# Create your models here.
class Directore(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.nombre} {self.apellido} {self.nacionalidad}'


class Genero(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.nombre} '


class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    f_estreno = models.DateField()
    duracion = models.TimeField()
    sinopsis = models.CharField(max_length=255)
    calificacion = models.IntegerField()
    director = models.ForeignKey(Directore, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Domicilio {self.id}: {self.titulo} {self.f_estreno} {self.duracion} {self.sinopsis} {self.calificacion}'


class Serie(models.Model):
    titulo = models.CharField(max_length=255)
    f_inicio = models.DateField()
    f_fin = models.DateField(null=True)
    temporadas = models.IntegerField()
    sinopsis = models.CharField(max_length=255)
    calificacion = models.IntegerField()
    director = models.ForeignKey(Directore, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Domicilio {self.id}: {self.titulo} {self.f_inicio} {self.f_fin} {self.temporadas} {self.sinopsis} {self.calificacion}'
