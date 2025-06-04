from django import forms
from productos.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre_producto', 'descripcion']
        widgets = {
            'id_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
