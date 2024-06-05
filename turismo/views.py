from django.shortcuts import render 

def index(request):
    return render(request, 'index.html')

def pagprueba2(request):
    return render(request, 'pagprueba2.html')

def pagprueba3(request):
    return render(request, 'pagprueba3.html')