from django.urls import path
from . import views

app_name = 'aerolinea'

urlpatterns = [
    path("", views.index, name="index"),
    ]