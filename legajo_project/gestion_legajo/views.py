from django.shortcuts import render

def docente_dashboard(request):
    return render(request, 'gestion_legajo/docente_dashboard.html')

def alumno_dashboard(request):
    return render(request, 'gestion_legajo/alumno_dashboard.html')

def admin_dashboard(request):
    return render(request, 'gestion_legajo/admin_dashboard.html')
