from django import forms

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length = 100)
    descriptcion = forms.CharField(max_length = 100)
    fecha_estreno = forms.DateField()

    
class LibroFormulario(forms.Form):
    nombre = forms.CharField(max_length = 100)
    descripcion = forms.CharField(max_length = 100)
    autor = forms.CharField(max_length = 100)
    fecha_publicacion = forms.DateField()

    
class SerieFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    fecha_estreno = forms.DateField()
    temporadas = forms.IntegerField()
    cant_capitulos = forms.IntegerField()
