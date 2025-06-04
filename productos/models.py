from django.db import models

class Producto(models.Model):
    id_producto = models.CharField(max_length=20, unique=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_producto