from django.urls import path
from . import views

app_name = 'aerolinea'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    ]