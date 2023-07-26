from django.forms import ModelForm, EmailInput, TextInput, TimeInput, DateInput, FileInput
from .models import Directore, Genero, Pelicula, Serie

class DirectoreForm(ModelForm):
    class Meta:
        model = Directore
        fields = '__all__'

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        widgets = {
            'f_estreno': DateInput(attrs={'type': 'date'}),
            'duracion': TextInput(attrs={'type': 'number'}),
            'calificacion': TextInput(attrs={'type': 'number'}),
            'portada': FileInput(attrs={'accept': 'image/*'})
        }

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'
        widgets = {
            'f_inicio': DateInput(attrs={'type': 'date'}),
            'f_fin': DateInput(attrs={'type': 'date'}),
            'temporadas': TextInput(attrs={'type': 'number'}),
            'calificacion': TextInput(attrs={'type': 'number'}),
            'portada': FileInput(attrs={'accept': 'image/*'})
        }