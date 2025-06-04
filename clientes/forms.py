from django import forms
from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
        'nombre_fantasia', 
        'razon_social', 
        'correo', 
        'direccion_despacho'
        ]
