from django.db import models

class Producto(models.Model):
    MATERIAL_CHOICES = [
        ('papel', 'Papel'),
        ('plastico', 'Plástico'),
        ('biodegradable', 'Biodegradable'),
        ('tnt', 'TNT'),
    ]

    TAMAÑO_CHOICES = [
        ('pequeña', 'Pequeña'),
        ('mediana', 'Mediana'),
        ('grande', 'Grande'),
    ]

    COLOR_CHOICES = [
        ('blanco', 'Blanco'),
        ('negro', 'Negro'),
        ('kraft', 'Kraft'),
        ('transparente', 'Transparente'),
    ]

    id_producto = models.AutoField(unique=True, primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    tipo_material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='kraft')
    tamaño = models.CharField(max_length=20, choices=TAMAÑO_CHOICES, default='grande')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='blanco')
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    coste_producción_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    precio_venta_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.nombre_producto} ({self.tamaño}, {self.tipo_material})"
