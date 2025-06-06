from django.contrib import admin
from django.urls import path, include
from pedidos.views import crear_pedido, añadir_abono, listar_pedidos, listar_pedidos_filtrados

urlpatterns = [
    path('crear/', crear_pedido, name='crear_pedido'),
    path('lista/', listar_pedidos, name='listar_pedidos'),
    path('<int:cod_pedido>/abonar/', añadir_abono, name='añadir_abono'),
    path('<str:estado>/', listar_pedidos_filtrados, name='listar_pedidos_filtrados'),
]