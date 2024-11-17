from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('DOC', 'Docente'),
        ('ALU', 'Alumno')
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='ALU')
class Docente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    costo_por_hora = models.DecimalField(max_digits=5, decimal_places=2)

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    contenido = models.TextField()
    modalidad = models.CharField(max_length=50, choices=[('PRESENCIAL', 'Presencial'), ('VIRTUAL', 'Virtual')])
    sede = models.CharField(max_length=100)
    docentes = models.ManyToManyField(Docente)



