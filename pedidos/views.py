from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidoForm, AbonoForm, DetallePedido, DetallePedidoForm
from .models import Pedido, Abono


def crear_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        detalle_form = DetallePedidoForm(request.POST)

        if pedido_form.is_valid() and detalle_form.is_valid():
            pedido = pedido_form.save()  # ya no usamos commit=False ni generamos uuid

            producto = detalle_form.cleaned_data['producto']
            cantidad = detalle_form.cleaned_data['cantidad']

            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=cantidad
            )

            return redirect('listar_pedidos')
    else:
        pedido_form = PedidoForm()
        detalle_form = DetallePedidoForm()

    return render(request, 'pedidos/crear_pedido.html', {
        'form': pedido_form,
        'detalle_form': detalle_form
    })

def añadir_abono(request, cod_pedido):
    pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)

    if request.method == 'POST':
        form = AbonoForm(request.POST)
        if form.is_valid():
            abono = form.save(commit=False)
            abono.pedido = pedido
            abono.save()
            return redirect('listar_pedidos')  # vuelve a la lista después de guardar
    else:
        form = AbonoForm()

    return render(request, 'pedidos/añadir_abono.html', {
        'form': form,
        'pedido': pedido,
    })

def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-cod_pedido')
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})