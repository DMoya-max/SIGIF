from django.shortcuts import render

def index(request):
    
    return render(request,"dashboard/index.html")

def mant(request):

    return render(request, "mant.html")