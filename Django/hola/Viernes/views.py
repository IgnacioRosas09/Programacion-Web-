from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indice(request):
    return render(request, 'Viernes/Pregunta.html')

def indiceParam(request, date):
    return render(request, 'Viernes/Dia.html', {'nombre': date.capitalize()})
    