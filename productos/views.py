from django.shortcuts import render, redirect
from .forms import ProductoForm
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