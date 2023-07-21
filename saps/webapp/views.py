from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from peliculas.models import Pelicula, Directore


#from personas.models import Participante, Domicilio


# Create your views here.
def bienvenido(request):
    #busqueda = request.POST.get('buscar')
    #no_personas = Participante.objects.count()
    #li_personas = Participante.objects.all()
    #no_domicilio = Domicilio.objects.count()
    #li_domicilio = Domicilio.objects.all()
    # buscar personas
    #if busqueda:
        #li_personas = Participante.objects.filter(
            #Q(nombre__icontains=busqueda) |
            #Q(apellido__icontains=busqueda) |
            #Q(email__icontains=busqueda)
        #).distinct()
        #if li_personas:
            #return render(request, 'crudPersona.html', {'no_personas': no_personas, 'li_personas': li_personas})
        #li_domicilio = Domicilio.objects.filter(
            #Q(calle__icontains=busqueda) |
            #Q(no_calle__icontains=busqueda) |
            #Q(pais__icontains=busqueda)
        #).distinct()
        #if li_domicilio:
            #return render(request, 'crudDomicilio.html', {'no_domicilios': no_domicilio , 'li_domicilios': li_domicilio})
    return render(request, 'bienvenido.html')


def crudDirectore(request):
    busqueda = request.POST.get('buscar')
    no_directores = Directore.objects.count()
    li_directores = Directore.objects.all()
    #buscar personas
    if busqueda:
        li_personas = Directore.objects.filter(
            Q(nombre__icontains= busqueda) |
            Q(apellido__icontains= busqueda) |
            Q(nacionalidad__icontains= busqueda)
            ).distinct()

    return render(request, 'crudDirectore.html', {'no_directores': no_directores, 'li_directores': li_directores})


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

def prueba(request):
    return render(request, 'sistemaSolar.html')

def crudDomicilio(request):
    busqueda = request.POST.get('buscar')
    no_domicilio = Domicilio.objects.count()
    li_domicilio = Domicilio.objects.all()
    # buscar personas
    if busqueda:
        li_domicilio = Domicilio.objects.filter(
            Q(calle__icontains=busqueda) |
            Q(no_calle__icontains=busqueda) |
            Q(pais__icontains=busqueda)
        ).distinct()
    return render(request, 'crudDomicilio.html', {'no_domicilios': no_domicilio , 'li_domicilios': li_domicilio})

