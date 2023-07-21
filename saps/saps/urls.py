"""
URL configuration for saps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from peliculas.views import detallePelicula, editarPelicula, detalleDirectore, nuevoDirectore, editarDirectore, \
    eliminarDirectore
from webapp.views import bienvenido, crudPelicula, crudDirectore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('persona', crudPelicula, name='indexPelicula'),
    path('detalle_persona/<int:id>', detallePelicula),
    # path('nueva_persona', nuevaParticipante),
    path('editar_persona/<int:id>', editarPelicula),
    # path('eliminar_persona/<int:id>', eliminarParticipante),
    # path('domicilio', crudDomicilio, name='indexDomicilio'),
    # path('detalle_domicilio/<int:id>', detalleDomicilio),
    # path('nuevo_domicilio', nuevoDomicilio),
    # path('editar_domicilio/<int:id>', editarDomicilio),
    # path('eliminar_domicilio/<int:id>', eliminarDomicilio),
    path('director', crudDirectore, name='indexDirectore'),
    path('detalle_directore/<int:id>', detalleDirectore),
    path('nuevo_directore', nuevoDirectore),
    path('editar_directore/<int:id>', editarDirectore),
    path('eliminar_directore/<int:id>', eliminarDirectore),
]
