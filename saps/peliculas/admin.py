from django.contrib import admin

# Register your models here.
from peliculas.models import Directore, Serie, Pelicula, Genero

admin.site.register(Directore)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Serie)
