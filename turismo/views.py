from django.shortcuts import render
from .models import Alumno, Genero

def pagprueba2(request):
    return render(request, 'pagprueba2.html/')

def pagprueba3(request):
    return render(request, 'pagprueba3.html/')

def login(request):
    return render(request, 'login.html/')

def index_alumn(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'index_alumn.html',context)