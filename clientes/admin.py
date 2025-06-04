from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cod_cliente', 'nombre_fantasia', 'razon_social', 'correo', 'direccion_despacho')
    search_fields = ('cod_cliente', 'nombre_fantasia', 'razon_social', 'correo')
    list_filter = ('nombre_fantasia',)
    ordering = ('cod_cliente',)

admin.site.register(Cliente, ClienteAdmin)
# Register your models here.
