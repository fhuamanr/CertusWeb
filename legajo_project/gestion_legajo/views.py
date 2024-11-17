from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Curso
from .forms import UserForm, CursoForm
from django.contrib.auth import get_user_model

User = get_user_model()  # Obtiene el modelo de usuario personalizado configurado en AUTH_USER_MODEL

def home(request):
    return render(request, 'gestion_legajo/home.html')

def docente_dashboard(request):
    return render(request, 'gestion_legajo/docente_dashboard.html')

def alumno_dashboard(request):
    return render(request, 'gestion_legajo/alumno_dashboard.html')

def admin_dashboard(request):
    return render(request, 'gestion_legajo/admin_dashboard.html')

def gestion_usuarios(request):
    usuarios = User.objects.all()  # Usa el modelo personalizado
    return render(request, 'gestion_legajo/gestion_usuarios.html', {'usuarios': usuarios})

def gestion_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion_legajo/gestion_cursos.html', {'cursos': cursos})

def agregar_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Cifrar la contraseña
            user.save()
            return redirect('gestion_usuarios')  # Redirigir a la gestión de usuarios
    else:
        form = UserForm()
    return render(request, 'gestion_legajo/agregar_usuario.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_cursos')
    else:
        form = CursoForm()
    return render(request, 'gestion_legajo/agregar_curso.html', {'form': form})
