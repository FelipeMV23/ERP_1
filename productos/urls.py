from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),

]
