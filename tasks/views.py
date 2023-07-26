from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

@login_required
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

@login_required
def detail_task(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'error': 'no se pudo editar la tarea'
            })
        
    
@login_required
def complete_tasks(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def tasks_complete(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.delete()
        return redirect('tasks')


@login_required
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