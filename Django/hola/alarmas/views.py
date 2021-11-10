from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse 

alarmas = ['6:50', '7:00']
# Create your views here.

def index(request):
    return render(request, 'alarmas/index.html',{'alarmas':alarmas})

def v2(request):
    if request.method == 'POST':
        form = FNuevaAlarma(request.POST)
        if form.is_valid():
            alarma = form.cleaned_data['alarma']
            alarmas.append(alarma)
            return HttpResponseRedirect(reverse('alarmas:index'))
        else:
            return render(request, 'alarmas/v2.html', {'cont_form': form})
    else:
        return render(request, 'alarmas/v2.html', {'cont_form':FNuevaAlarma()})

class FNuevaAlarma(forms.Form):
    alarma = forms.CharField(label='Programar alarma')
    #snooze = forms.IntegerField(label='Repetir', min_value=0, max_value=0)