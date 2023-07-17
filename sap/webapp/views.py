from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return render(request, 'bienvenido.html')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('Email: jgarcia@grupoasd.com Celular: +57 3213019066')
