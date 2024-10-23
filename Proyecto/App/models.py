from django.db import models

# Create your models here.

class Productos(models.Model):
    #---> PK
    Codigo=models.AutoField(primary_key=True)
    #---> Nombre del Producto
    Nombre=models.TextField(max_length=50)
    #---> Cantidad/Stock
    Cantidad=models.TextField(max_length=15)
    #---> Ubicacion de donde va a ir situado. (interior o exterior)
    Ubicacion=models.TextField(max_length=20)
    #---> Imagen del Producto
    Imagen=models.ImageField(upload_to="Personajes",null=True)

    def __int__(self):
        self.Codigo