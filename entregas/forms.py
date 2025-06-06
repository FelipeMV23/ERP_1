from django import forms
from .models import Entrega

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['cantidad_entregada']
        widgets = {
            'cantidad_entregada': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
        }