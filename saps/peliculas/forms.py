from django.forms import ModelForm, TextInput, DateInput, FileInput
from .models import Directore, Genero, Pelicula, Serie
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    is_superuser = forms.BooleanField()


