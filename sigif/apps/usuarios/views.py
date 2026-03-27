
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UsuarioForm
from .models import Usuarios

def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get("user")
        contra = request.POST.get("clave")

        if usuario == "admin" and contra == "123":
            messages.success(request, "Bienvenido al sistema")
            return redirect("dashboard")  
        else:
            messages.error(request, "Usuario o contraseña incorrecto")
            return render(request, "usuarios/login.html")

    return render(request, "usuarios/login.html")

def usuarios(request):

    return render(request, "usuarios/usuarios.html")

def crear_usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm ()
    return render(request, "usuarios/usuarios.html",  {'form': form})

def listar_usuarios(request):
    users = Usuarios.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'users': users})

def editar_usuarios(request, id):
    users = get_object_or_404(Usuarios, id=id)
    if request.method == 'POST':
        users = UsuarioForm(request.POST, instance=Usuarios)
        if  users.is_valid():
            pass
    