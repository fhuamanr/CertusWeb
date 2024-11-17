from django import forms
from django.contrib.auth.models import User
from .models import Curso,CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']  # Incluye el campo 'role'
        widgets = {
            'password': forms.PasswordInput(),
        }
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'contenido', 'modalidad', 'sede']