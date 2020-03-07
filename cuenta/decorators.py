from django.http import HttpResponse
from django.shortcuts import redirect


def usuarioNoAutenticado(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('cuenta:inicio')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def usuarioPermitido(rolesPermitidos=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            grupo = None

            if request.user.groups.exists():
                grupo = request.user.groups.all()[0].name

            if grupo in rolesPermitidos:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No está autorizado para ver esta página')

        return wrapper_func
    return decorator


def soloAdmin(view_func):
    def wrapper_func(request, *args, **kwargs):
        grupo = None

        if request.user.groups.exists():
            grupo = request.user.groups.all()[0].name

        if grupo == 'Cliente':
            return redirect('cuenta:usuario')

        if grupo == 'Admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
