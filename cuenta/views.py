from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from cuenta.models import Cliente, Orden, Producto, Etiqueta
from cuenta.forms import OrdenForm, RegistrarUsuarioForm, ClienteForm
from cuenta.filters import OrdenFilter
from cuenta.decorators import usuarioNoAutenticado, usuarioPermitido, soloAdmin


@usuarioNoAutenticado
def registrarse(request):
    form = RegistrarUsuarioForm()

    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'La cuenta ha sido registrada para ' + username)

            return redirect('cuenta:iniciarSesion')

    contexto = {'form': form}

    return render(request, 'cuenta/registrarse.html', contexto)


@usuarioNoAutenticado
def iniciarSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)

            return redirect('cuenta:inicio')
        else:
            messages.info(request, 'Username o Password incorrecto')

    contexto = {}

    return render(request, 'cuenta/iniciarSesion.html', contexto)


def cerrarSesion(request):
    logout(request)

    return redirect('cuenta:iniciarSesion')


@login_required(login_url='cuenta:iniciarSesion')
@soloAdmin
def inicio(request):
    ordenes = Orden.objects.all()
    clientes = Cliente.objects.all()
    totalClientes = clientes.count()
    totalOrdenes = ordenes.count()
    entregados = ordenes.filter(estado='Entregado').count()
    pendientes = ordenes.filter(estado='Pendiente').count()
    contexto = {
        'ordenes': ordenes,
        'clientes': clientes,
        'totalOrdenes': totalOrdenes,
        'entregados': entregados,
        'pendientes': pendientes
    }

    return render(request, 'cuenta/dashboard.html', contexto)


@login_required(login_url='cuenta:iniciarSesion')
@usuarioPermitido(rolesPermitidos=['Cliente'])
def opcionCuenta(request):
    cliente = request.user.cliente
    form = ClienteForm(instance=cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)

        if form.is_valid():
            form.save()

    contexto = {'form': form}

    return render(request, 'cuenta/cuenta.html', contexto)


@login_required(login_url='cuenta:iniciarSesion')
@usuarioPermitido(rolesPermitidos=['Admin'])
def productos(request):
    productos = Producto.objects.all()

    return render(request, 'cuenta/productos.html', {'productos': productos})


def usuario(request):
    ordenes = request.user.cliente.orden_set.all()
    totalOrdenes = ordenes.count()
    entregados = ordenes.filter(estado='Entregado').count()
    pendientes = ordenes.filter(estado='Pendiente').count()
    contexto = {
        'ordenes': ordenes,
        'totalOrdenes': totalOrdenes,
        'entregados': entregados,
        'pendientes': pendientes
    }

    return render(request, 'cuenta/usuario.html', contexto)


@login_required(login_url='cuenta:iniciarSesion')
@usuarioPermitido(rolesPermitidos=['Admin'])
def cliente(request, idCliente):
    cliente = Cliente.objects.get(id=idCliente)
    ordenes = cliente.orden_set.all()
    totalOrdenes = ordenes.count()
    filtro = OrdenFilter(request.GET, queryset=ordenes)
    ordenes = filtro.qs
    contexto = {
        'cliente': cliente,
        'ordenes': ordenes,
        'totalOrdenes': totalOrdenes,
        'filtro': filtro
    }

    return render(request, 'cuenta/cliente.html', contexto)


@login_required(login_url='cuenta:iniciarSesion')
@usuarioPermitido(rolesPermitidos=['Admin'])
def registrarOrden(request):
    form = OrdenForm()

    if request.method == 'POST':
        form = OrdenForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    contexto = {'form': form}

    return render(request, 'cuenta/registrarOrden.html', contexto)


@login_required(login_url='cuenta:iniciarSesion')
@usuarioPermitido(rolesPermitidos=['Admin'])
def actualizarOrden(request, idOrden):
    orden = Orden.objects.get(id=idOrden)
    form = OrdenForm(instance=orden)

    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)

        if form.is_valid():
            form.save()

            return redirect('/')

    contexto = {'form': form}

    return render(request, 'cuenta/registrarOrden.html', contexto)


@login_required(login_url='cuenta:iniciarSesion')
@usuarioPermitido(rolesPermitidos=['Admin'])
def eliminarOrden(request, idOrden):
    orden = Orden.objects.get(id=idOrden)

    if request.method == "POST":
        orden.delete()

        return redirect('/')

    contexto = {'orden': orden}

    return render(request, 'cuenta/eliminar.html', contexto)
