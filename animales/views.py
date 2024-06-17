from django.shortcuts import render

def index_ani(request):
    return render(request, 'index_ani.html/')

def tienda_ani(request):
    return render(request, 'tienda_ani.html/')

def adopcion_ani(request):
    return render(request, 'adopcion_ani.html/')

def nosotros_ani(request):
    return render(request, 'nosotros_ani.html/')

def contacto_ani(request):
    return render(request, 'contacto_ani.html/')

def reg_ini_sesion_ani(request):
    return render(request, 'reg_ini_sesion_ani.html/')

def pago_ani(request):
    return render(request, 'pago_ani.html/')
