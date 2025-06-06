from django import forms
from .models import Entrega
from pedidos.models import DetallePedido

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['detalle_pedido', 'cantidad_entregada']
        widgets = {
            'detalle_pedido': forms.Select(attrs={'class': 'form-select'}),
            'cantidad_entregada': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }

    def __init__(self, *args, **kwargs):
        pedido = kwargs.pop('pedido', None)
        super().__init__(*args, **kwargs)
        if pedido:
            self.fields['detalle_pedido'].queryset = pedido.detalles.all()
        else:
            self.fields['detalle_pedido'].queryset = DetallePedido.objects.none()