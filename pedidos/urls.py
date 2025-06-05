from django.contrib import admin
from django.urls import path, include
from pedidos.views import crear_pedido, añadir_abono, listar_pedidos

urlpatterns = [
    path('crear/', crear_pedido, name='crear_pedido'),
    path('lista/', listar_pedidos, name='listar_pedidos'),
    path('pedidos/<int:cod_pedido>/abonar/', añadir_abono, name='añadir_abono'),
]