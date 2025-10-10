from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Noticia
from .forms import NoticiaForm

class NoticiaList(ListView):
    model = Noticia
    template_name = "informacion/noticia_list.html"

class NoticiaCreate(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = "informacion/form.html"
    success_url = reverse_lazy("informacion:noticia_list")

class NoticiaUpdate(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = "informacion/form.html"
    success_url = reverse_lazy("informacion:noticia_list")

class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = "informacion/confirm_delete.html"
    success_url = reverse_lazy("informacion:noticia_list")
