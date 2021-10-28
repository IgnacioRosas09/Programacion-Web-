from django.shortcuts import render

alarmas = ['6:50', '7:00']
# Create your views here.

def index(request):
    return render(request, 'alarmas/index.html',{'alarmas':alarmas})

def v2(request):
    return render(request, 'alarmas/v2.html')