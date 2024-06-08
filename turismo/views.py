from django.shortcuts import render

def pagprueba2(request):
    return render(request, 'pagprueba2.html/')

def pagprueba3(request):
    return render(request, 'pagprueba3.html/')

def login(request):
    return render(request, 'login.html/')