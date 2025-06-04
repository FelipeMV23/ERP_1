from django.db import models
from clientes.models import Cliente
from productos.models import Producto

class Pedido(models.Model):
    cod_pedido = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido {self.cod_pedido} - {self.cliente.nombre_fantasia}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto.nombre_producto} x {self.cantidad}"

class Entrega(models.Model):
    detalle_pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE, related_name='entregas')
    fecha_entrega = models.DateField(auto_now_add=True)
    cantidad_entregada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad_entregada} entregado de {self.detalle_pedido.producto.nombre_producto}"

class Abono(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='abonos')
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Abono de {self.monto} para {self.pedido.cod_pedido}"
    
class Entrega(models.Model):
    detalle_pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE, related_name='entregas')
    fecha_entrega = models.DateField(auto_now_add=True)
    cantidad_entregada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad_entregada} entregado de {self.detalle_pedido.producto.nombre_producto}"
