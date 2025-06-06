from django.db import models
from pedidos.models import DetallePedido

class Entrega(models.Model):
    detalle_pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE, related_name='entregas')
    fecha_entrega = models.DateField(auto_now_add=True)
    cantidad_entregada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.detalle_pedido.producto.nombre} - {self.cantidad_entregada} entregado(s)"
