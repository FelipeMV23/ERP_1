from django import forms
from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Esto incluye todos los campos del modelo

