from django.urls import path
from . import views

urlpatterns = [
    path('indice/<str:date>', views.indiceParam, name='indice'),
    path('indice', views.indice, name='indice')
    ]