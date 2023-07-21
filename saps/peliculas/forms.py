from django.forms import ModelForm, EmailInput, TextInput
from .models import Directore, Genero, Pelicula, Serie

class DirectoreForm(ModelForm):
    class Meta:
        model = Directore
        fields = '__all__'

class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        widgets = {
        }
