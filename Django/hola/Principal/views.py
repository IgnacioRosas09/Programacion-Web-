from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaDjango(request):
    return HttpResponse("Hola Django!")

def pepe(request):
    return HttpResponse("Hola Pepe!")

def holaTu(request, nombre):
    return HttpResponse('Hola {nombre.capitalize()}!')