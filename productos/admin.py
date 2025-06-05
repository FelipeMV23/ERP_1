from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre_producto', 'tipo_material', 'tamaño', 'color', 'stock', 'precio_unitario')
    search_fields = ('id_producto', 'nombre_producto', 'tipo_material', 'color')
    list_filter = ('tipo_material', 'tamaño', 'color')
    ordering = ('nombre_producto',)

admin.site.register(Producto, ProductoAdmin)