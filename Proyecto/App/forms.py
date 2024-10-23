# ---> Importación de 'FORMS'
from django import forms
#---> Importación de Models
from .models import * 
#---> Validaciones
from django.forms import ValidationError

class NuevoProducto(forms.ModelForm):

    def verificaciones(self):
        Codigo=self.cleaned_data['Codigo']
        validacion=Productos.objects.filter(Codigo=Codigo).exists()

        if validacion:
            raise ValidationError("Codigo ya Registrado")
    
    class Meta:
        model=Productos
        fields='__all__'