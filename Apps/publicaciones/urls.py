from django.urls import path
from . import views

app_name = "publicaciones"

urlpatterns = [
    path('', views.ArticuloList.as_view(), name="index"),
    # Publicadores
    path("publicadores/", views.PublicadorList.as_view(), name="publicador_list"),
    path("publicadores/crear/", views.PublicadorCreate.as_view(), name="publicador_create"),
    path("publicadores/<int:pk>/editar/", views.PublicadorUpdate.as_view(), name="publicador_update"),
    path("publicadores/<int:pk>/eliminar/", views.PublicadorDelete.as_view(), name="publicador_delete"),

    # Autorizadores
    path("autorizadores/", views.AutorizadorList.as_view(), name="autorizador_list"),
    path("autorizadores/crear/", views.AutorizadorCreate.as_view(), name="autorizador_create"),
    path("autorizadores/<int:pk>/editar/", views.AutorizadorUpdate.as_view(), name="autorizador_update"),
    path("autorizadores/<int:pk>/eliminar/", views.AutorizadorDelete.as_view(), name="autorizador_delete"),

    # Artículos
    path("articulos/", views.ArticuloList.as_view(), name="articulo_list"),
    path("articulos/crear/", views.ArticuloCreate.as_view(), name="articulo_create"),
    path("articulos/<int:pk>/", views.ArticuloDetail.as_view(), name="articulo_detail"),
    path("articulos/<int:pk>/editar/", views.ArticuloUpdate.as_view(), name="articulo_update"),
    path("articulos/<int:pk>/eliminar/", views.ArticuloDelete.as_view(), name="articulo_delete"),
]
