
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('iniciar_sesion')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('', include('usuarios.urls')),
    path('', root_redirect),  # ruta vacía redirige a iniciar_sesion
    path('', include('usuarios.urls')), 
 

]

