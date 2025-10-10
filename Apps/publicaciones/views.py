from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from .models import EstudiantePublicador, EstudianteAutorizador, Articulo, Comentario
from .forms import EstudiantePublicadorForm, EstudianteAutorizadorForm, ArticuloForm, ComentarioForm

# --- PUBLICADORES ---
class PublicadorList(ListView):
    model = EstudiantePublicador
    template_name = "publicaciones/publicador_list.html"

class PublicadorCreate(CreateView):
    model = EstudiantePublicador
    form_class = EstudiantePublicadorForm
    template_name = "publicaciones/form.html"
    success_url = reverse_lazy("publicaciones:publicador_list")

class PublicadorUpdate(UpdateView):
    model = EstudiantePublicador
    form_class = EstudiantePublicadorForm
    template_name = "publicaciones/form.html"
    success_url = reverse_lazy("publicaciones:publicador_list")

class PublicadorDelete(DeleteView):
    model = EstudiantePublicador
    template_name = "publicaciones/confirm_delete.html"
    success_url = reverse_lazy("publicaciones:publicador_list")

# --- AUTORIZADORES ---
class AutorizadorList(ListView):
    model = EstudianteAutorizador
    template_name = "publicaciones/autorizador_list.html"

class AutorizadorCreate(CreateView):
    model = EstudianteAutorizador
    form_class = EstudianteAutorizadorForm
    template_name = "publicaciones/form.html"
    success_url = reverse_lazy("publicaciones:autorizador_list")

class AutorizadorUpdate(UpdateView):
    model = EstudianteAutorizador
    form_class = EstudianteAutorizadorForm
    template_name = "publicaciones/form.html"
    success_url = reverse_lazy("publicaciones:autorizador_list")

class AutorizadorDelete(DeleteView):
    model = EstudianteAutorizador
    template_name = "publicaciones/confirm_delete.html"
    success_url = reverse_lazy("publicaciones:autorizador_list")

# --- ARTÍCULOS ---
class ArticuloList(ListView):
    model = Articulo
    template_name = "publicaciones/articulo_list.html"

class ArticuloDetail(DetailView):
    model = Articulo
    template_name = "publicaciones/articulo_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = self.object
            comentario.save()
            messages.success(request, "Comentario agregado correctamente")
            return redirect("publicaciones:articulo_detail", pk=self.object.pk)
        return self.get(request, *args, **kwargs)

class ArticuloCreate(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = "publicaciones/form.html"
    success_url = reverse_lazy("publicaciones:articulo_list")

class ArticuloUpdate(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = "publicaciones/form.html"
    success_url = reverse_lazy("publicaciones:articulo_list")

class ArticuloDelete(DeleteView):
    model = Articulo
    template_name = "publicaciones/confirm_delete.html"
    success_url = reverse_lazy("publicaciones:articulo_list")
