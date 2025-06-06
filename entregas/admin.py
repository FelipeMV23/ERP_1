from django.contrib import admin
from .models import Entrega

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('detalle_pedido', 'fecha_entrega', 'cantidad_entregada')
    list_filter = ('fecha_entrega',)
    search_fields = ('detalle_pedido__producto__nombre_producto',)