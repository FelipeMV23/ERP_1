from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import EntregaForm
from pedidos.models import Pedido

def registrar_entrega(request, cod_pedido):
    pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)

    if request.method == 'POST':
        form = EntregaForm(request.POST, pedido=pedido)
        if form.is_valid():
            entrega = form.save(commit=False)
            detalle = entrega.detalle_pedido  # ya viene del form

            if entrega.cantidad_entregada > detalle.cantidad_pendiente:
                messages.error(request, f"No puedes entregar más de lo pendiente ({detalle.cantidad_pendiente}).")
            else:
                entrega.save()
                messages.success(request, "Entrega registrada correctamente.")
                return redirect('listar_pedidos')
    else:
        form = EntregaForm(pedido=pedido)

    return render(request, 'entregas/registrar_entrega.html', {
        'pedido': pedido,
        'form': form,
    })