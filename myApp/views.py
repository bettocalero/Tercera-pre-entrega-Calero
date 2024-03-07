from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "myApp/inicio.html")

def agregar_pelicula(request):

    return render(request, 'myApp/nueva_pelicula.html')

def agregar_serie(request):
    
    return render(request, 'nueva_serie.html')

def agregar_libro(request):
    
    return render(request, 'nuevo_libro.html')

