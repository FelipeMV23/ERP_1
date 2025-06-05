
from django.contrib import admin
from django.urls import path, include
from productos.views import agregar_productos, consultar_productos, editar_producto, eliminar_producto

urlpatterns = [
    path('agregar/', agregar_productos, name='agregar_productos'),
    path('consultar/', consultar_productos, name='consultar_productos'),
    path('editar/<int:id_producto>/', editar_producto, name='editar_productos'),
    path('eliminar/<int:id_producto>/', eliminar_producto, name='eliminar_productos'),


]
