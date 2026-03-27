from django.shortcuts import render

def inventario(request):

    return render(request, "inventario/inventario.html")

def inv_historial(request):

    return render(request, "inventario/inv_historial.html")

def inv_control(request):

    return render(request, "inventario/inv_control.html")