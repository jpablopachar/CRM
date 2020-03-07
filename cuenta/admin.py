from django.contrib import admin
from cuenta.models import Cliente, Producto, Orden, Etiqueta

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Etiqueta)
