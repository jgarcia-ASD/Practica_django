# Practica_django
Este repositorio está diseñado específicamente para practicar y adquirir habilidades en el manejo del framework Django, basado en Python. Aquí encontrarás ejercicios y proyectos que te permitirán explorar las características y funcionalidades de Django. A través de la práctica

## enfoque rama
esta rama esta hecha con apoyo de un video de youtube el cual la idea es implementar aparte del crud verificacion de usuarios y hacer un despliegue en un server basado en la nube

### futuras explicaciones de cambios
#### ahorrar codigo
podemos implementar un import para importar todas las vistas y no añadir una por una esto eesta en urls
```python
from task import tasks
```
#### crear usuarios 
django ya ofrece esto si usamos lo siguiente en el archivo views de nuestra app
```python
from django.contrib.auth.forms import UserCreationForm
```

#### podemos tener una base html 
para usarlo como plantilla  asi otras paginas heredan lo que tengamos en nuestra pantilla principal
```python
{% block content %}

{% endblock %}
```