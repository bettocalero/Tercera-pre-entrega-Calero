from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "myApp/inicio.html")

def agregar_pelicula(request):

    if request.method == 'POST':
        formulario = PeliculaFormulario(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data

            nueva_pelicula = Pelicula(nombre = info_dict['nombre'],
                                      descriptcion = info_dict['descriptcion'],
                                      fecha_estreno = info_dict['fecha_estreno'])
            
            nueva_pelicula.save()

            return render(request, 'myApp/inicio.html')
    
    else:
        formulario = PeliculaFormulario()

    return render(request, 'myApp/nueva_pelicula.html', {'form' : formulario})

def agregar_serie(request):

    if request.method == 'POST':

        formulario = SerieFormulario(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data

            nueva_serie = Serie(nombre = info_dict['nombre'],
                                descripcion = info_dict['descripcion'],
                                fecha_estreno = info_dict['fecha_estreno'],
                                temporadas = info_dict['temporadas'],
                                cant_capitulos = info_dict['cant_capitulos'])
            
            nueva_serie.save()

            return render(request, 'myApp/inicio.html')
        
    else:
        formulario = SerieFormulario
    
    return render(request, 'myApp/nueva_serie.html', {'form' : formulario})

def agregar_libro(request):

    if request.method == 'POST':

        formulario = LibroFormulario(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data

            nueva_pelicula = Libro(nombre = info_dict['nombre'],
                                      descripcion = info_dict['descripcion'],
                                      autor = info_dict['autor'],
                                      fecha_publicacion = info_dict['fecha_publicacion'])
            
            nueva_pelicula.save()

            return render(request, 'myApp/inicio.html')
        
    else:
        formulario = LibroFormulario()
    
    return render(request, 'myApp/nuevo_libro.html', {'form' : formulario})


def buscar_libro(request):

    return render(request, 'myApp/buscar_libro.html')

def resultado_libro(request):

    libro = request.GET['libro']

    resultado = Libro.objects.filter(nombre__iexact=libro)

    return render(request, 'myApp/resultado_libro.html', {'resultado' : resultado})

