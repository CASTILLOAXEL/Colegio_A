from django.urls import path
from . import views

app_name = "informacion"

urlpatterns = [

    path('', views.NoticiaList.as_view(), name="index"),

    path("noticias/", views.NoticiaList.as_view(), name="noticia_list"),
    path("noticias/crear/", views.NoticiaCreate.as_view(), name="noticia_create"),
    path("noticias/<int:pk>/editar/", views.NoticiaUpdate.as_view(), name="noticia_update"),
    path("noticias/<int:pk>/eliminar/", views.NoticiaDelete.as_view(), name="noticia_delete"),
]
