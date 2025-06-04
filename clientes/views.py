from django.shortcuts import render, redirect
from clientes.forms import ClienteForm


def crear_cliente(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar_clientes')
    
    else:
        form = ClienteForm()
    
    return(render(request, 'clientes/crear_cliente.html', {'form':form}))