import time

from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from peliculas.models import Pelicula, Directore, Genero

from peliculas.forms import DirectoreForm, GeneroForm, PeliculaForm


# Create your views here.
# vistas Directores
def detalleDirectore(request, id):
    # persona = Persona.objects.get(pk=id)
    directore = get_object_or_404(Directore, pk=id)
    return render(request, 'directore/detalle.html', {'directore': directore})


def nuevoDirectore(request):
    if request.method == 'POST':
        formaDirectore = DirectoreForm(request.POST)
        if formaDirectore.is_valid():
            formaDirectore.save()
            return redirect('indexDirectore')
    else:
        formaDirectore = DirectoreForm()

    return render(request, 'directore/nuevo.html', {'formaDirectore': formaDirectore})


def editarDirectore(request, id):
    directore = get_object_or_404(Directore, pk=id)
    if request.method == 'POST':
        formaDirectore = DirectoreForm(request.POST, instance=directore)
        if formaDirectore.is_valid():
            formaDirectore.save()
            return redirect('indexDirectore')
    else:
        formaDirectore = DirectoreForm(instance=directore)

    return render(request, 'directore/editar.html', {'formaDirectore': formaDirectore})


def eliminarDirectore(request, id):
    directore = get_object_or_404(Directore, pk=id)
    if directore:
        directore.delete()
    return redirect('indexDirectore')


# vistas Generos
def detalleGenero(request, id):
    # persona = Persona.objects.get(pk=id)
    genero = get_object_or_404(Genero, pk=id)
    return render(request, 'genero/detalle.html', {'genero': genero})


def nuevoGenero(request):
    if request.method == 'POST':
        formaGenero = GeneroForm(request.POST)
        if formaGenero.is_valid():
            formaGenero.save()
            return redirect('indexGenero')
    else:
        formaGenero = GeneroForm()

    return render(request, 'genero/nuevo.html', {'formaGenero': formaGenero})


def editarGenero(request, id):
    genero = get_object_or_404(Genero, pk=id)
    if request.method == 'POST':
        formaGenero = GeneroForm(request.POST, instance=genero)
        if formaGenero.is_valid():
            formaGenero.save()
            return redirect('indexGenero')
    else:
        formaGenero = GeneroForm(instance=genero)

    return render(request, 'genero/editar.html', {'formaGenero': formaGenero})


def eliminarGenero(request, id):
    genero = get_object_or_404(Genero, pk=id)
    if genero:
        genero.delete()
    return redirect('indexGenero')


# vistas peliculas
def detallePelicula(request, id):
    # persona = Persona.objects.get(pk=id)
    pelicula = get_object_or_404(Pelicula, pk=id)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})


# PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPelicula(request):
    if request.method == 'POST':
        formaPelicula = PeliculaForm(request.POST, request.FILES)
        if formaPelicula.is_valid():
                formaPelicula.save()
                return redirect('indexPelicula')
    else:
        formaPelicula = PeliculaForm()

    return render(request, 'peliculas/nuevo.html', {'formaPelicula': formaPelicula})


def editarPelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    if request.method == 'POST':
        formaPelicula = PeliculaForm(request.POST, instance=pelicula)
        if formaPelicula.is_valid():
            formaPelicula.save()
            return redirect('indexPelicula')
    else:
        formaPelicula = PeliculaForm(instance=pelicula)

    return render(request, 'peliculas/editar.html', {'formaPelicula': formaPelicula})


def eliminarPelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    if pelicula:
        pelicula.delete()
    return redirect('indexPelicula')
