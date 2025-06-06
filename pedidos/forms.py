from django import forms
from .models import Pedido, DetallePedido, Abono
from django.forms import modelformset_factory

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
        exclude = ['pedido']

DetallePedidoFormSet = modelformset_factory(
    DetallePedido,
    fields=('producto', 'cantidad'),
    extra=1,  # Cantidad de productos que quieres mostrar inicialmente
    can_delete=True  # Para permitir borrar detalles si quieres
)