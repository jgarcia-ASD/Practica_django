# Practica_django

Este repositorio está diseñado específicamente para practicar y adquirir habilidades en el manejo del framework Django,
basado en Python. Aquí encontrarás ejercicios y proyectos que te permitirán explorar las características y
funcionalidades de Django. A través de la práctica

## enfoque rama

esta rama esta hecha para simular en ejercicio sin video o ayuda solo isntrucciones la idea es hacerlo solo con mi
conocimiento sobre django e irlo eriqueciendo a medida que pasa el tiempo

### futuras explicaciones de cambios

#### ahorrar codigo

podemos implementar un import para importar todas las vistas y no añadir una por una esto esta en urls y se le puede
poner un apodo asi podemos evitar confuciones

```python
from peliculas import views as peliculas_views
from webapp import views as webapp_views
```

#### crear usuarios

django ya ofrece esto si usamos lo siguiente en el archivo views de nuestra app

```python
from django.contrib.auth.forms import UserCreationForm
```

#### base html

para usarlo como plantilla asi otras paginas heredan lo que tengamos en nuestra pantilla principal

```python
{ % block content %}

{ % endblock %}
```

#### conexion con una base de datos

esta es una conexion a una bd de sql
````python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'StreamingDjango',
        'USER': 'root',
        'PASSWORD': '*************',
        'HOST': '********',
        'PORT': '3306',
    }
}
````

#### funcion con inicio de sesion obligatorio

para  hacer que si o si algunos usuario tengan que inicar sesion podemos importar una biblioteca y 'proteger' las 
funciones que deseemos
````python
from django.contrib.auth.decorators import login_required

@login_required
def ejemplo(request):
    print('esto esta preotegido')
````

#### esconder html a los no registrados

si no has iniciado sesion se te puede ocultar cierto contenido (no es lo mismo al anterior ya que el anterior protege 
las funciones este protege el contenifo html) y esto se realiza mediante un if que valida si ya inicio sesion

````python
{% if user.is_authenticated %}

{% endif %}
````