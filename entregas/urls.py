from django.contrib import admin
from django.urls import path, include
from entregas.views import registrar_entrega

urlpatterns = [
    path('entregas/registrar/<int:cod_pedido>/', registrar_entrega, name='registrar_entrega')
]