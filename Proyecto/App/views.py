from django.shortcuts import render,get_object_or_404,redirect

#---->Importamos el Sector de Formularios
from .forms import *
from .models import *

#--->Importamos la Libreria de Logout
from django.contrib.auth import logout

#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.
def Home(request):
    return render(request, 'index.html')

# Partes que se necesitan permisos para poder acceder 
@login_required

def Agregar(request):
    data={
        'forms':NuevoProducto()
    }
    if request.method=='POST':
        query=NuevoProducto(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Registrados"
        else:
            data['forms']=NuevoProducto
    return render (request,'Pages/agregar.html',data)

def salir(request):
    logout(request)
    return redirect(to='home')