from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from peliculas.models import Pelicula, Directore, Genero


#from personas.models import Participante, Domicilio


# Create your views here.
def bienvenido(request):
    li_pelicula = Pelicula.objects.all()
    return render(request, 'bienvenido.html', {'li_pelicula': li_pelicula})


def crudDirectore(request):
    busqueda = request.POST.get('buscar')
    no_directores = Directore.objects.count()
    li_directores = Directore.objects.all()
    #buscar
    if busqueda:
        li_directores = Directore.objects.filter(
            Q(nombre__icontains= busqueda) |
            Q(apellido__icontains= busqueda) |
            Q(nacionalidad__icontains= busqueda)
            ).distinct()

    return render(request, 'crudDirectore.html', {'no_directores': no_directores, 'li_directores': li_directores})

def crudGenero(request):
    busqueda = request.POST.get('buscar')
    no_generos = Genero.objects.count()
    li_generos = Genero.objects.all()
    #buscar
    if busqueda:
        li_generos = Genero.objects.filter(
            Q(nombre__icontains= busqueda)
            ).distinct()

    return render(request, 'crudGenero.html', {'no_generos': no_generos, 'li_generos': li_generos})


def crudPelicula(request):
    busqueda = request.POST.get('buscar')
    no_pelicula = Pelicula.objects.count()
    li_pelicula = Pelicula.objects.all()
    #buscar personas
    if busqueda:
        li_personas = Pelicula.objects.filter(
            Q(titulo__icontains= busqueda) |
            Q(f_estreno__icontains= busqueda) |
            Q(duracion__icontains= busqueda) |
            Q(sinopsis__icontains= busqueda) |
            Q(calificacion__icontains= busqueda)
            ).distinct()

    return render(request, 'crudPelicula.html', {'no_pelicula':no_pelicula , 'li_pelicula': li_pelicula})



