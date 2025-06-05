from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ProductoForm
from django.shortcuts import get_object_or_404
from productos.forms import ProductoForm
from productos.models import Producto

# Create your views here.
def agregar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar_productos')  # Cambia esta ruta si tienes otra URL de destino
    else:
        form = ProductoForm()
    
    return render(request, 'productos/agregar_productos.html', {'form': form})

def consultar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consultar_productos.html', {'productos': productos})

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('consultar_productos')  # Cambia por tu nombre de URL para listar clientes
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'productos/editar_productos.html', {'form': form, 'producto': producto})


from django.contrib import messages

def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        nombre = producto.nombre_producto
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado exitosamente.')
    return redirect('consultar_productos')



