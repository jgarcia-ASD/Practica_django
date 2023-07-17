from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def bienvenido(request):
    no_personas = Persona.objects.count()
    return render(request, 'bienvenido.html', {'no_personas':no_personas})

def prueba(request):
    return render(request, 'sistemaSolar.html')
