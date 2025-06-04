from django.urls import path
from productos.views import agregar_producto, buscar_productos, editar_producto, eliminar_producto

urlpatterns = [
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('buscar/', buscar_productos, name='buscar_productos'),
    path('editar/<int:id>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
]
