from django.shortcuts import get_object_or_404, render, redirect
from clientes.forms import ClienteForm
from clientes.models import Cliente

#Crea al cliente a partir de ClienteForm. Si el formulario es Válido, te envía al listado o consulta de clientes

def crear_cliente(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar_clientes')
    else:
        form = ClienteForm()
    
    return(render(request, 'clientes/crear_clientes.html', {'form':form}))

#Recupera los datos del modelo Cliente y los envía en pantalla a través de un diccionario
def consultar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/consultar_clientes.html', {'clientes': clientes})

#Utiliza la misma lógica que crear_cliente para la edición de ciertos datos
def editar_cliente(request, cod_cliente):
    cliente = get_object_or_404(Cliente, cod_cliente=cod_cliente)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('consultar_clientes')  # Cambia por tu nombre de URL para listar clientes
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes/editar_clientes.html', {'form': form, 'cliente': cliente})

#Borra al cliente usando delete(). para hacer esto, captura la ID que sería cod_cliente

def eliminar_cliente(request, cod_cliente):
    cliente = get_object_or_404(Cliente, cod_cliente=cod_cliente)
    if request.method == 'POST':
        cliente.delete()
    return redirect('consultar_clientes')

