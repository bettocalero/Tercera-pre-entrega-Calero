from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.inicio),
    path("nueva_pelicula/", views.agregar_pelicula),
    path("nueva_serie/", views.agregar_serie),
    path("nuevo_libro/", views.agregar_libro),
]
