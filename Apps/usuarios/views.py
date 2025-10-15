from django.shortcuts import render

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Usuario
from .forms import UsuarioRegistroForm, LoginForm

# Registro de usuarios
def registro(request):
    if request.method == "POST":
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f"✅ Usuario {usuario.username} registrado correctamente")
            login(request, usuario)
            return redirect("home:index")
        else:
            messages.error(request, "❌ Error al registrar. Revisa los datos ingresados.")
    else:
        form = UsuarioRegistroForm()
    return render(request, "usuarios/registro.html", {"form": form})


# Login
def login_usuario(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f"Bienvenido {usuario.first_name} {usuario.last_name}")
            return redirect("home:index")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, "usuarios/login.html", {"form": form})

# Logout
def logout_usuario(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente")
    return redirect("usuarios:login")

# Listado de usuarios (requiere login)
@login_required(login_url="usuarios:login")
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios/usuario_list.html", {"usuarios": usuarios})
