
from django.shortcuts import render, redirect
from django.contrib import messages

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