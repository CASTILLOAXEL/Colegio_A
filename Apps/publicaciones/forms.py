from django import forms
from .models import EstudiantePublicador, EstudianteAutorizador, Articulo, Comentario

class EstudiantePublicadorForm(forms.ModelForm):
    class Meta:
        model = EstudiantePublicador
        fields = "__all__"

class EstudianteAutorizadorForm(forms.ModelForm):
    class Meta:
        model = EstudianteAutorizador
        fields = "__all__"

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = "__all__"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["estudiante", "texto"]
