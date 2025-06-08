from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

@login_required(login_url='sesion_cerrada')
def navbar(request):
    return render(request, 'usuarios/nav.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        if not username_or_email or not password:
            messages.error(request, 'Ingrese usuario/correo y contraseña.', extra_tags='login_error')
        else:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
            except User.DoesNotExist:
                username = username_or_email

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                next_url = request.GET.get('next', 'listar_pedidos')
                return redirect(next_url)
            else:
                messages.error(request, 'Credenciales inválidas.', extra_tags='login_error')

    return render(request, 'usuarios/iniciar_sesion.html')

@login_required(login_url='sesion_cerrada')


@login_required(login_url='sesion_cerrada')
@require_POST
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

