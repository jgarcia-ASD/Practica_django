from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from peliculas.models import Pelicula, Directore

from peliculas.forms import DirectoreForm


# Create your views here.
#vistas Directores
def detalleDirectore(request, id):
    #persona = Persona.objects.get(pk=id)
    directore = get_object_or_404(Directore, pk=id)
    return render(request, 'directore/detalle.html', {'directore':directore})


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
    domicilio = get_object_or_404(Directore, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('indexDirectore')



#vistas peliculas
def detallePelicula(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Pelicula, pk=id)
    return render(request, 'personas/pelicula.html', {'persona': persona})

#PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPelicula(request):
    if request.method == 'POST':
        formaPelicula = PeliculaForm(request.POST)
        if formaPelicula.is_valid():
            formaPelicula.save()
            return redirect('indexPersona')
    else:
        formaPersona = PeliculaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPelicula})

def editarPelicula(request, documento):
    persona = get_object_or_404(Participante, pk=documento)
    if request.method == 'POST':
        formaPersona = ParticipanteForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = ParticipanteForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def eliminarPelicula(request, documento):
    persona = get_object_or_404(Participante, pk=documento)
    if persona:
        persona.delete()
    return redirect('indexPersona')