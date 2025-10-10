from django.db import models

# Create your models here.
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
