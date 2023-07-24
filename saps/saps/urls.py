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
from django.conf import settings
from django.conf.urls.static import static

from peliculas.views import detallePelicula,editarPelicula, nuevaPelicula, eliminarPelicula, detalleDirectore, nuevoDirectore, editarDirectore, \
    eliminarDirectore, detalleGenero, nuevoGenero, editarGenero, eliminarGenero
from webapp.views import bienvenido, crudPelicula, crudDirectore, crudGenero

urlpatterns = [
    path('admin/', admin.site.urls),
    path('director', crudDirectore, name='indexDirectore'),
    path('detalle_directore/<int:id>', detalleDirectore),
    path('nuevo_directore', nuevoDirectore),
    path('editar_directore/<int:id>', editarDirectore),
    path('eliminar_directore/<int:id>', eliminarDirectore),
    path('genero', crudGenero, name='indexGenero'),
    path('detalle_genero/<int:id>', detalleGenero),
    path('nuevo_genero', nuevoGenero),
    path('editar_genero/<int:id>', editarGenero),
    path('eliminar_genero/<int:id>', eliminarGenero),
    path('', bienvenido, name='index'),
    path('pelicula', crudPelicula, name='indexPelicula'),
    path('detalle_pelicula/<int:id>', detallePelicula),
    path('nueva_pelicula', nuevaPelicula),
    path('editar_pelicula/<int:id>', editarPelicula),
    path('eliminar_pelicula/<int:id>', eliminarPelicula),
    # path('domicilio', crudDomicilio, name='indexDomicilio'),
    # path('detalle_domicilio/<int:id>', detalleDomicilio),
    # path('nuevo_domicilio', nuevoDomicilio),
    # path('editar_domicilio/<int:id>', editarDomicilio),
    # path('eliminar_domicilio/<int:id>', eliminarDomicilio),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)