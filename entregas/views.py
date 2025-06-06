from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import EntregaForm
from pedidos.models import DetallePedido

def registrar_entrega(request, detalle_id):
    detalle = get_object_or_404(DetallePedido, id=detalle_id)

    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad_entregada']
            if cantidad > detalle.cantidad_pendiente:
                messages.error(request, f"No puedes entregar más de lo pendiente ({detalle.cantidad_pendiente}).")
            else:
                form.instance.detalle_pedido = detalle
                form.save()
                messages.success(request, "Entrega registrada correctamente.")
                return redirect('listar_pedidos')
    else:
        form = EntregaForm()

    return render(request, 'entregas/registrar_entrega.html', {
        'detalle': detalle,
        'form': form,
    })