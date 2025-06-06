from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidoForm, AbonoForm, DetallePedido, DetallePedidoForm, DetallePedidoFormSet
from .models import Pedido, Abono
from django.forms import modelformset_factory
from collections import defaultdict

def crear_pedido(request):
    DetallePedidoFormSet = modelformset_factory(
        DetallePedido,
        form=DetallePedidoForm,
        extra=1,
        can_delete=False
    )

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        detalle_formset = DetallePedidoFormSet(request.POST, queryset=DetallePedido.objects.none())

        if pedido_form.is_valid() and detalle_formset.is_valid():
            pedido = pedido_form.save()

            # Agrupar productos repetidos
            productos_agrupados = defaultdict(int)
            for form in detalle_formset:
                producto = form.cleaned_data.get('producto')
                cantidad = form.cleaned_data.get('cantidad')

                if producto and cantidad:
                    productos_agrupados[producto] += cantidad

            # Crear solo un DetallePedido por producto
            for producto, cantidad_total in productos_agrupados.items():
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=cantidad_total
                )

            return redirect('listar_pedidos')
    else:
        pedido_form = PedidoForm()
        detalle_formset = DetallePedidoFormSet(queryset=DetallePedido.objects.none())

    return render(request, 'pedidos/crear_pedido.html', {
        'form': pedido_form,
        'detalle_formset': detalle_formset
    })

def añadir_abono(request, cod_pedido):
    pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)

    if request.method == 'POST':
        form = AbonoForm(request.POST)
        if form.is_valid():
            abono = form.save(commit=False)
            abono.pedido = pedido  # Asociar el abono al pedido correcto
            abono.save()
            return redirect('listar_pedidos')
    else:
        form = AbonoForm()

    return render(request, 'pedidos/añadir_abono.html', {'form': form, 'pedido': pedido})

def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-cod_pedido')
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})

def listar_pedidos_filtrados(request, estado):
    pedidos = Pedido.objects.all()

    if estado == 'por_pagar':
        pedidos = [p for p in pedidos if not p.esta_pagado]
    elif estado == 'pagados':
        pedidos = [p for p in pedidos if p.esta_pagado]

    return render(request, 'pedidos/listar_pedidos.html', {
        'pedidos': pedidos,
        'estado': estado
    })