from django.db import models

# Create your models here.
from django.db import models

class EstudiantePublicador(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    carnet = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class EstudianteAutorizador(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    carnet = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(blank=True)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(EstudiantePublicador, on_delete=models.CASCADE)
    autorizado_por = models.ForeignKey(EstudianteAutorizador, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios")
    estudiante = models.CharField(max_length=120)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.estudiante} en {self.articulo.titulo}"
