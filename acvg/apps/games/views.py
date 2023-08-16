from django.shortcuts import render

# Create your views here.
def prueba(request):
    return render(request, 'games/preloader.html')

def Cubo(request):
    return render(request, 'games/basic.html')