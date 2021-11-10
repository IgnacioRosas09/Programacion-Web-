from django.shortcuts import render
from django import forms

alarmas = ['6:50', '7:00']
# Create your views here.

def index(request):
    return render(request, 'alarmas/index.html',{'alarmas':alarmas})

def v2(request):
    return render(request, 'alarmas/v2.html', {'cont_form':FNuevaAlarma()})

class FNuevaAlarma(forms.Form):
    alarma = forms.CharField(label='Programar alarma')
    #snooze = forms.IntegerField(label='Repetir', min_value=0, max_value=0)