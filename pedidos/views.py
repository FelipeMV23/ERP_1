from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidoForm, AbonoForm, DetallePedido, DetallePedidoForm, DetallePedidoFormSet
from .models import Pedido, Abono
from django.forms import modelformset_factory
from collections import defaultdict
from django.contrib import messages

#modelformset_factory sirve para poder replicar los detalles del pedido (es decir, el producto y la cantidad) cuantas veces quiera el usuario
#Si la solicitud del post es correcta, se instancian pedido_form y detalle_formset, ya que el pedido completo está segmentado en distintos models
#Luego viene una validación que verifica que si se añadió el mismo producto, se sume para no generar ruido en la información
#La siguiente validación es la que verifica que haya mínimo un producto y mínimo una cantidad mayor a cero
#Luego se guardan en la base de datos, y se manejan los formularios inválidos
#Se finaliza con el render

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
            productos_agrupados = defaultdict(int)
            productos_validos = 0

            for form in detalle_formset:
                if form.cleaned_data:
                    producto = form.cleaned_data.get('producto')
                    cantidad = form.cleaned_data.get('cantidad')

                    if producto and cantidad and cantidad > 0:
                        productos_agrupados[producto] += cantidad
                        productos_validos += 1

            if productos_validos == 0:
                messages.error(request, "Debe agregar al menos un producto con cantidad mayor a 0.")
            else:
                # Guarda el pedido sin monto_total aún
                pedido = pedido_form.save(commit=False)

                # Calcula el monto total sumando cantidad * precio unitario
                monto_total = sum(
                    cantidad * producto.precio_venta_unitario for producto, cantidad in productos_agrupados.items()
                )

                pedido.monto_total = monto_total
                pedido.save()

                # Guarda los detalles con cantidades agrupadas
                for producto, cantidad_total in productos_agrupados.items():
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=producto,
                        cantidad=cantidad_total
                    )

                messages.success(request, f"Pedido creado con monto total ${monto_total:.2f}")
                return redirect('listar_pedidos')
        else:
            messages.error(request, "Formulario inválido. Por favor revise los campos.")
    else:
        pedido_form = PedidoForm()
        detalle_formset = DetallePedidoFormSet(queryset=DetallePedido.objects.none())

    return render(request, 'pedidos/crear_pedido.html', {
        'form': pedido_form,
        'detalle_formset': detalle_formset
    })


#El abono se valida a partir del cod_pedido, y luego del monto_total

def añadir_abono(request, cod_pedido):
    pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)

    if request.method == 'POST':
        form = AbonoForm(request.POST)
        if form.is_valid():
            abono = form.save(commit=False)
            monto = abono.monto

            if monto <= 0:
                messages.error(request, "El monto del abono debe ser mayor que 0.")
            elif monto > pedido.saldo_pendiente:
                messages.error(request, f"El monto del abono (${monto}) excede el saldo pendiente (${pedido.saldo_pendiente}).")
            else:
                abono.pedido = pedido
                abono.save()
                messages.success(request, "Abono registrado correctamente.")
                return redirect('listar_pedidos')
        else:
            messages.error(request, "Formulario inválido. Verifique los datos ingresados.")
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


def eliminar_pedido(request, cod_pedido):
    pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)
    pedido.delete()
    messages.success(request, f'El pedido {cod_pedido} fue eliminado correctamente.')
    return redirect('listar_pedidos')  # Asegúrate que esta URL esté bien definida