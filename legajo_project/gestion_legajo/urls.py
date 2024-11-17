from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('perfil/docente/', views.docente_dashboard, name='docente_dashboard'),
    path('perfil/alumno/', views.alumno_dashboard, name='alumno_dashboard'),
    path('perfil/administrador/', views.admin_dashboard, name='admin_dashboard'),
    path('perfil/administrador/usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('perfil/administrador/usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('perfil/administrador/cursos/', views.gestion_cursos, name='gestion_cursos'),
    path('perfil/administrador/cursos/agregar/', views.agregar_curso, name='agregar_curso'),
]