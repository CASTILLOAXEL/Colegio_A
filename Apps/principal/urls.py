from django.urls import path
from . import views

app_name = "principal"

urlpatterns = [
    path('', views.index, name="index"),
    path("categorias/", views.CategoriaList.as_view(), name="categoria_list"),
    path("categorias/crear/", views.CategoriaCreate.as_view(), name="categoria_create"),
    path("categorias/<int:pk>/editar/", views.CategoriaUpdate.as_view(), name="categoria_update"),
    path("categorias/<int:pk>/eliminar/", views.CategoriaDelete.as_view(), name="categoria_delete"),
]
