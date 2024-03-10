from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.inicio, name='inicio'),
    path("nueva_pelicula/", views.agregar_pelicula, name='pelicula'),
    path("nueva_serie/", views.agregar_serie, name='serie'),
    path("nuevo_libro/", views.agregar_libro, name= 'libro'),
    path("buscar_libro/", views.buscar_libro, name='buscar_libro'),
    path("resultado/", views.resultado_libro, name='resultado'),
]
