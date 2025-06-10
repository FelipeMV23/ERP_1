from django import forms
from .models import Pedido, DetallePedido, Abono
from django.forms import modelformset_factory

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'fecha_pedido']
        widgets = {
            'fecha_pedido': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
        }

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad']
        widgets = {
            'total_producto': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control-plaintext'}),
        }

class AbonoForm(forms.ModelForm):
    class Meta:
        model = Abono
        exclude = ['pedido']

DetallePedidoFormSet = modelformset_factory(
    DetallePedido,
    form=DetallePedidoForm,
    extra=1,
    can_delete=True
)
