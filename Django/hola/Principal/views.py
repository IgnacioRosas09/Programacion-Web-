from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaDjango(request):
    return HttpResponse("Hola Django!")