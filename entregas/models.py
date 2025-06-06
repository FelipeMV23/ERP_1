from django.db import models
from pedidos.models import DetallePedido
from django.db.models import Sum

class Entrega(models.Model):
    detalle_pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE, related_name='entregas')
    fecha_entrega = models.DateField(auto_now_add=True)
    cantidad_entregada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad_entregada} entregado de {self.detalle_pedido.producto.nombre_producto}"


@property
def cantidad_entregada(self):
    return self.entregas.aggregate(total=Sum('cantidad_entregada'))['total'] or 0

@property
def cantidad_pendiente(self):
    return max(0, self.cantidad - self.cantidad_entregada)