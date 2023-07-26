from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe'
                })
    return render(request, 'signup.html', {
        'form': UserCreationForm,
        'error': 'no cionciden las contraseñas'
    })

def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def createtasks(request):

    if request.method == 'GET':
        return render(request, 'created_task.html', {
            'form': TaskForm
        })
    else: 
        try:
            form = TaskForm(request.POST)
            new_tasks = form.save(commit=False)
            new_tasks.user = request.user
            new_tasks.save()
            return redirect ('tasks')
        except ValueError:
            return render(request, 'created_task.html', {
                'form': TaskForm,
                'error': 'no se pudo crear la tarea'
            })

def signout(request):
    logout(request)
    return redirect ('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signin.html', {
                'form' : AuthenticationForm,
                'error': 'usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('tasks')