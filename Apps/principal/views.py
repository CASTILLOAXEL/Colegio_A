from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categoria
from .forms import CategoriaForm
from django.shortcuts import render
def index(request):
    return render(request, "principal/index.html")

class CategoriaList(ListView):
    model = Categoria
    template_name = "principal/categoria_list.html"

class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "principal/form.html"
    success_url = reverse_lazy("principal:categoria_list")

class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "principal/form.html"
    success_url = reverse_lazy("principal:categoria_list")

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "principal/confirm_delete.html"
    success_url = reverse_lazy("principal:categoria_list")
