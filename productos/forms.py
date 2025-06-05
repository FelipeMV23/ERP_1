from django import forms
from .models import Producto

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre_producto',
            'tipo_material',  # se renderiza como <select>
            'tamaño',         # se renderiza como <select>
            'color',          # se renderiza como <select>
            'descripcion',
            'stock',
            'precio_unitario',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

        labels = {
            'id_producto': 'Código del producto',
            'nombre_producto': 'Nombre',
            'tipo_material': 'Tipo de material',
            'tamaño': 'Tamaño',
            'color': 'Color',
            'descripcion': 'Descripción',
            'stock': 'Stock disponible',
            'precio_unitario': 'Precio unitario ($)',
        }
