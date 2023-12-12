from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from Servidor.Libros.librosapp.models import Libro
from django.views.generic.edit import UpdateView , DeleteView

# Create your views here.

class ListList(ListView):
    model = Libro
    template_name = 'libros/libro_list.html'


class LibroDetalle(DetailView):

    model = Libro
    template_name = 'libros/libro_details.html'

class EditarLibro(UpdateView):
    model=Libro
    fields=["titulo", "autores", "editorial","genero", "resumen"]
    template_name ="libros/libro_edit.html"
    success_url= reverse_lazy("libro_list")



class Delete(DeleteView):
    model = Libro
    fields=["titulo", "autores", "editorial","genero", "resumen"]
    template_name ="libros/libro_delete.html"
    success_url = reverse_lazy("libro_list")
