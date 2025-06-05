from django import forms
from .models import Pedido, DetallePedido, Abono

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'monto_total']

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad']

class AbonoForm(forms.ModelForm):
    class Meta:
        model = Abono
        fields = ['pedido', 'monto']