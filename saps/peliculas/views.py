import time

from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pelicula, Directore, Genero, Serie

from .forms import DirectoreForm, GeneroForm, PeliculaForm, SerieForm


# Create your views here.
# vistas Directores

@login_required
def nuevoDirectore(request):
    if request.method == 'POST':
        formaDirectore = DirectoreForm(request.POST)
        if formaDirectore.is_valid():
            nombre = formaDirectore.cleaned_data['nombre']
            apellido = formaDirectore.cleaned_data['nombre']
            if Directore.objects.filter(nombre=nombre, apellido=apellido).exists():
                error = 'Ya existe este director'
                return render(request, 'directore/nuevo.html', {
                    'formaDirectore': formaDirectore,
                    'eror': error
                })
            else:
                formaDirectore.save()
                messages.success(request, 'Se guardo perfectamente')
                return redirect('indexDirectore')
        else:
            error = 'No se guardó en la base de datos. Verifica los campos.'
            return render(request, 'directore/nuevo.html', {
               'formaGenero': formaDirectore,
               'error': error
        })
    else:
        formaDirectore = DirectoreForm()

    return render(request, 'directore/nuevo.html', {'formaDirectore': formaDirectore})


@login_required
def editarDirectore(request, id):
    directore = get_object_or_404(Directore, pk=id)
    if request.method == 'POST':
        formaDirectore = DirectoreForm(request.POST, instance=directore)
        if formaDirectore.is_valid():
            formaDirectore.save()
            messages.success(request, 'Se edito perfectamente')
            return redirect('indexDirectore')
    else:
        formaDirectore = DirectoreForm(instance=directore)

    return render(request, 'directore/editar.html', {'formaDirectore': formaDirectore})


@login_required
def eliminarDirectore(request, id):
    directore = get_object_or_404(Directore, pk=id)
    if directore:
        directore.delete()
        messages.success(request, 'Se elimino perfectamente')
    return redirect('indexDirectore')


# vistas Generos

@login_required
def nuevoGenero(request):
    if request.method == 'POST':
        formaGenero = GeneroForm(request.POST)
        if formaGenero.is_valid():
            nombre = formaGenero.cleaned_data['nombre']
            if Genero.objects.filter(nombre=nombre).exists():
                error = 'Ya existe este genero'
                return render(request, 'genero/nuevo.html', {
                    'formaGenero': formaGenero,
                    'error': error
                })
            else:
                formaGenero.save()
                messages.success(request, 'Se guardo perfectamente')
                return redirect('indexGenero')
        else:
            error = 'No se guardó en la base de datos. Verifica los campos.'
            return render(request, 'genero/nuevo.html', {
                'formaGenero': formaGenero,
                'error': error
            })
    else:
        formaGenero = GeneroForm()

    return render(request, 'genero/nuevo.html', {'formaGenero': formaGenero})


@login_required
def editarGenero(request, id):
    genero = get_object_or_404(Genero, pk=id)
    if request.method == 'POST':
        formaGenero = GeneroForm(request.POST, instance=genero)
        if formaGenero.is_valid():
            formaGenero.save()
            messages.success(request, 'Se edito perfectamente')
            return redirect('indexGenero')
    else:
        formaGenero = GeneroForm(instance=genero)

    return render(request, 'genero/editar.html', {'formaGenero': formaGenero})


@login_required
def eliminarGenero(request, id):
    genero = get_object_or_404(Genero, pk=id)
    if genero:
        genero.delete()
        messages.success(request, 'Se elimino perfectamente')
    return redirect('indexGenero')


# vistas peliculas
# PersonaForm = modelform_factory(Persona, exclude=[])

@login_required
def nuevaPelicula(request):
    if request.method == 'POST':
        formaPelicula = PeliculaForm(request.POST, request.FILES)

        if formaPelicula.is_valid():
            titulo = formaPelicula.cleaned_data['titulo']
            calificaion = formaPelicula.cleaned_data['calificacion']
            temporadas = formaPelicula.cleaned_data['temporadas']
            portada = formaPelicula.cleaned_data['portada']
            if Pelicula.objects.filter(titulo=titulo).exists():
                error = 'Ya existe una película con este título.'
                return render(request, 'peliculas/nuevo.html', {
                    'formaPelicula': formaPelicula,
                    'error': error
                })
            elif calificaion > 10 or calificaion < 0:
                error = 'la calificacion no esta en el rango permitido.'
                return render(request, 'series/nuevo.html', {
                'formaSerie': formaPelicula,
                    'error': error
                })
            elif temporadas < 1:
                error = 'las temporadas no esta en el rango permitido.'
                return render(request, 'series/nuevo.html', {
                'formaSerie': formaPelicula,
                'error': error
            })
            elif portada is None:
                portada = 'imagenes/no_disponible.png'
                formaSerie = Serie(
                    titulo=titulo,
                    f_inicio=formaPelicula.cleaned_data['f_inicio'],
                    f_fin=formaPelicula.cleaned_data['f_fin'],
                    temporadas=temporadas,
                    sinopsis=formaPelicula.cleaned_data['sinopsis'],
                    calificacion=calificaion,
                    portada=portada,
                    director=formaPelicula.cleaned_data['director'],
                    genero=formaPelicula.cleaned_data['genero']
                )
                formaSerie.save()
                messages.success(request, 'Se guardo perfectamente en Base de datos')
                return redirect('indexSerie')
            else:
                formaPelicula.save()
                messages.success(request, 'Se guardo perfectamente en Base de datos' )
                return redirect('indexPelicula')
        else:
            error = 'No se guardó en la base de datos. Verifica los campos.'
            return render(request, 'peliculas/nuevo.html', {
                'formaPelicula': formaPelicula,
                'error': error
            })
    else:
        formaPelicula = PeliculaForm()

    return render(request, 'peliculas/nuevo.html', {'formaPelicula': formaPelicula})


@login_required
def editarPelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    if request.method == 'POST':
        formaPelicula = PeliculaForm(request.POST, instance=pelicula)
        if formaPelicula.is_valid():
            formaPelicula.save()
            messages.success(request, 'Se edito perfectamente')
            return redirect('indexPelicula')
    else:
        formaPelicula = PeliculaForm(instance=pelicula)

    return render(request, 'peliculas/editar.html', {'formaPelicula': formaPelicula})


@login_required
def eliminarPelicula(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    if pelicula:
        pelicula.delete()
        messages.success(request, 'Se elimino perfectamente')
    return redirect('indexPelicula')

# vistas peliculas

# PersonaForm = modelform_factory(Persona, exclude=[])

@login_required
def nuevaSerie(request):
    if request.method == 'POST':
        formaSerie = SerieForm(request.POST, request.FILES)
        if formaSerie.is_valid():
            titulo = formaSerie.cleaned_data['titulo']
            calificaion = formaSerie.cleaned_data['calificacion']
            temporadas = formaSerie.cleaned_data['temporadas']
            portada = formaSerie.cleaned_data['portada']
            if Serie.objects.filter(titulo=titulo).exists():
                error = 'Ya existe una serie con este título.'
                return render(request, 'series/nuevo.html', {
                    'formaSerie': formaSerie,
                    'error': error
                })
            elif calificaion > 10 or calificaion < 0:
                error = 'la calificacion no esta en el rango permitido.'
                return render(request, 'series/nuevo.html', {
                'formaSerie': formaSerie,
                    'error': error
                })
            elif temporadas < 1:
                error = 'las temporadas no esta en el rango permitido.'
                return render(request, 'series/nuevo.html', {
                'formaSerie': formaSerie,
                'error': error
            })
            elif portada is None:
                portada = 'imagenes/no_disponible.png'
                formaSerie = Serie(
                    titulo=titulo,
                    f_inicio=formaSerie.cleaned_data['f_inicio'],
                    f_fin=formaSerie.cleaned_data['f_fin'],
                    temporadas=temporadas,
                    sinopsis=formaSerie.cleaned_data['sinopsis'],
                    calificacion=calificaion,
                    portada=portada,
                    director=formaSerie.cleaned_data['director'],
                    genero=formaSerie.cleaned_data['genero']
                )
                formaSerie.save()
                messages.success(request, 'Se guardo perfectamente en Base de datos')
                return redirect('indexSerie')
            else:
                formaSerie.save()
                messages.success(request, 'Se guardo perfectamente en Base de datos')
                return redirect('indexSerie')
        else:
            error = 'No se guardó en la base de datos. Verifica los campos.'
            return render(request, 'series/nuevo.html', {
                'formaSerie': formaSerie,
                'error': error
            })
    else:
        formaSerie = SerieForm()

    return render(request, 'series/nuevo.html', {'formaSerie': formaSerie})



@login_required
def editarSerie(request, id):
    serie = get_object_or_404(Serie, pk=id)
    if request.method == 'POST':
        formaSerie = SerieForm(request.POST, request.FILES ,instance=serie)
        if formaSerie.is_valid():
            calificaion = formaSerie.cleaned_data['calificacion']
            temporadas = formaSerie.cleaned_data['temporadas']
            portada = formaSerie.cleaned_data['portada']
            if calificaion > 10 or calificaion < 0:
                error = 'la calificacion no esta en el rango permitido.'
                return render(request, 'series/nuevo.html', {
                    'formaSerie': formaSerie,
                    'error': error
                })
            elif temporadas < 1:
                error = 'las temporadas no esta en el rango permitido.'
                return render(request, 'series/nuevo.html', {
                    'formaSerie': formaSerie,
                    'error': error
                })
            elif portada is None:
                portada = 'imagenes/no_disponible.png'
                formaSerie = Serie(
                    titulo=formaSerie.cleaned_data['titulo'],
                    f_inicio=formaSerie.cleaned_data['f_inicio'],
                    f_fin=formaSerie.cleaned_data['f_fin'],
                    temporadas=temporadas,
                    sinopsis=formaSerie.cleaned_data['sinopsis'],
                    calificacion=calificaion,
                    portada=portada,
                    director=formaSerie.cleaned_data['director'],
                    genero=formaSerie.cleaned_data['genero']
                )
                formaSerie.save()
                messages.success(request, 'Se guardo perfectamente en Base de datos')
                return redirect('indexSerie')
            else:
                formaSerie.save()
                messages.success(request, 'Se guardo perfectamente en Base de datos')
                return redirect('indexSerie')
        else:
            error = 'No se guardó en la base de datos. Verifica los campos.'
            return render(request, 'series/nuevo.html', {
                'formaSerie': formaSerie,
                'error': error
            })
    else:
        formaSerie = SerieForm(instance=serie)

    return render(request, 'series/editar.html', {'formaSerie': formaSerie})


@login_required
def eliminarSerie(request, id):
    serie = get_object_or_404(Serie, pk=id)
    if serie:
        serie.delete()
        messages.success(request, 'Se elimino perfectamente')
    return redirect('indexSerie')
