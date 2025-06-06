from django.contrib import admin
from django.urls import path, include
from entregas.views import registrar_entrega

urlpatterns = [
    path('registrar/<int:detalle_id>/', registrar_entrega, name='registrar_entrega'),
]