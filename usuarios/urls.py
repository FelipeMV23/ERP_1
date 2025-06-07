from django.contrib import admin
from django.urls import path, include
from usuarios.views import iniciar_sesion, cerrar_sesion, navbar

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('navbar/', navbar, name='navbar'),
]
