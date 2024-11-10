from django.urls import path
from . import views

urlpatterns = [
    path('perfil/docente/', views.docente_dashboard, name='docente_dashboard'),
    path('perfil/alumno/', views.alumno_dashboard, name='alumno_dashboard'),
    path('perfil/administrador/', views.admin_dashboard, name='admin_dashboard'),
]