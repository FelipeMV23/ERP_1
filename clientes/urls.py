from django.contrib import admin
from django.urls import path, include
from clientes.views import crear_cliente

urlpatterns = [
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
]