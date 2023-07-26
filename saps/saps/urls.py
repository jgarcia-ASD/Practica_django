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

from peliculas import views as peliculas_views
from webapp import views as webapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicioSession/', webapp_views.signin, name='inicioSession'),
    path('crearSession/', webapp_views.signup, name='crearSession'),
    path('cerrarsession/', webapp_views.signout, name='cerrar'),
    path('director', webapp_views.crudDirectore, name='indexDirectore'),
    path('detalle_directore/<int:id>', peliculas_views.detalleDirectore),
    path('nuevo_directore', peliculas_views.nuevoDirectore),
    path('editar_directore/<int:id>', peliculas_views.editarDirectore),
    path('eliminar_directore/<int:id>', peliculas_views.eliminarDirectore),
    path('genero', webapp_views.crudGenero, name='indexGenero'),
    path('detalle_genero/<int:id>', peliculas_views.detalleGenero),
    path('nuevo_genero', peliculas_views.nuevoGenero),
    path('editar_genero/<int:id>', peliculas_views.editarGenero),
    path('eliminar_genero/<int:id>', peliculas_views.eliminarGenero),
    path('', webapp_views.bienvenido, name='index'),
    path('pelicula', webapp_views.crudPelicula, name='indexPelicula'),
    path('detalle_pelicula/<int:id>', peliculas_views.detallePelicula),
    path('nueva_pelicula', peliculas_views.nuevaPelicula),
    path('editar_pelicula/<int:id>', peliculas_views.editarPelicula),
    path('eliminar_pelicula/<int:id>', peliculas_views.eliminarPelicula),
    # path('domicilio', crudDomicilio, name='indexDomicilio'),
    # path('detalle_domicilio/<int:id>', detalleDomicilio),
    # path('nuevo_domicilio', nuevoDomicilio),
    # path('editar_domicilio/<int:id>', editarDomicilio),
    # path('eliminar_domicilio/<int:id>', eliminarDomicilio),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)