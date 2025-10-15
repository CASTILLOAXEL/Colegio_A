from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps.publicaciones.models import EstudiantePublicador, EstudianteAutorizador, Articulo, Comentario
from Apps.principal.models import Categoria

@login_required(login_url="usuarios:login")
def index(request):
    context = {
        "total_publicadores": EstudiantePublicador.objects.count(),
        "total_autorizadores": EstudianteAutorizador.objects.count(),
        "total_articulos": Articulo.objects.count(),
        "total_categorias": Categoria.objects.count(),
        "total_comentarios": Comentario.objects.count(),
        "ultimos_articulos": Articulo.objects.order_by("-fecha")[:5]
    }
    return render(request, "home/index.html", context)
