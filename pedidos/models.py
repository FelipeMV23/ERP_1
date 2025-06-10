from django.db import models
from clientes.models import Cliente
from productos.models import Producto
from decimal import Decimal
from django.db.models import Sum
from django.utils import timezone

class Pedido(models.Model):
    cod_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateTimeField(default=timezone.now)

    @property
    def saldo_pendiente(self):
        total_abonos = self.abonos.aggregate(total=Sum('monto'))['total'] or Decimal('0.00')
        return self.monto_total - total_abonos

    @property
    def esta_pagado(self):
        return self.saldo_pendiente <= 0

    def __str__(self):
        return f"Pedido {self.cod_pedido} - {self.cliente.nombre_fantasia}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total_producto = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    @property
    def total_entregado(self):
        return sum(entrega.cantidad_entregada for entrega in self.entregas.all())

    @property
    def cantidad_pendiente(self):
        return max(0, self.cantidad - self.total_entregado)

    @property
    def cantidad_entregada_total(self):
        return self.entregas.aggregate(total=models.Sum('cantidad_entregada'))['total'] or 0

    def save(self, *args, **kwargs):
        if self.producto and self.cantidad:
            self.total_producto = Decimal(self.cantidad) * self.producto.precio_venta_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto.nombre_producto} x {self.cantidad}"

class Abono(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='abonos')
    fecha = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Abono de {self.monto} para {self.pedido.cod_pedido}"
