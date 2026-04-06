
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
    users = Usuarios.objects.all()
    return render(request, 'usuarios/usuarios.html', {'users': users})
    

def crear_usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm ()
    return render(request, "usuarios/crear_usuarios.html",  {'form': form})


def editar_usuarios(request, id):
    user = get_object_or_404(Usuarios, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=user)
        if  form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm(instance=user)
    return render(request, 'usuarios/editar_usuarios.html', {'form': form})

def eliminar_usuario(request, id):
    user = get_object_or_404(Usuarios, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('usuarios')
    else:
        return render(request, 'usuarios/eliminar_usuario.html', {'user': user})