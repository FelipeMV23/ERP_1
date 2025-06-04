from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ProductoForm
from django.shortcuts import get_object_or_404
from productos.forms import ProductoForm
from productos.models import Producto

# Create your views here.
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Cambia esta ruta si tienes otra URL de destino
    else:
        form = ProductoForm()
    
    return render(request, 'productos/agregar_producto.html', {'form': form})

def buscar_productos(request):
    query = request.GET.get('q')
    resultados = Producto.objects.all()

    if query:
        resultados = resultados.filter(
            Q(nombre_producto__icontains=query) |
            Q(id_producto__icontains=query) |
            Q(descripcion__icontains=query)
        )

    return render(request, 'productos/buscar_productos.html', {
        'resultados': resultados,
        'query': query,
    })



def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('buscar_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})

from django.contrib import messages

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        nombre = producto.nombre_producto
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado exitosamente.')
    return redirect('buscar_productos')



