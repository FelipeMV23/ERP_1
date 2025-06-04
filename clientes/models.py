from django.db import models

class Cliente(models.Model):
    cod_cliente = models.AutoField(primary_key=True)
    nombre_fantasia = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100, unique=True)
    correo = models.EmailField()
    direccion_despacho = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_fantasia