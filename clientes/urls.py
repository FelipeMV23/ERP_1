from django.contrib import admin
from django.urls import path, include
from clientes.views import crear_cliente, consultar_clientes, editar_cliente

urlpatterns = [
    path('crear/', crear_cliente, name='crear_cliente'),
    path('listar/', consultar_clientes, name='consultar_clientes'),
    path('editar/<int:cod_cliente>/', editar_cliente, name='editar_cliente'),
]