from django.contrib import admin
from django.urls import path
from .views import * 


urlpatterns = [
    path('', Home, name='home'),  
    path('agregar/',Agregar,name='agregar'),
    path('logouts/',salir,name='logouts'),
]   