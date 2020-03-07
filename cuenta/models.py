from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)
    correo = models.CharField(max_length=200, null=True)
    imagen = models.ImageField(default="profile1.png", null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    CATEGORIA = (
        ('Interior', 'Interior'),
        ('Exterior', 'Exterior')
    )
    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField(null=True)
    categoria = models.CharField(max_length=200, null=True, choices=CATEGORIA)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, null=True)
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    ESTADO = (
        ('Pendiente', 'Pendiente'),
        ('Fuera para entregar', 'Fuera para entregar'),
        ('Entregado', 'Entregado'),
    )
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    fechaCreacion = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.CharField(max_length=200, null=True, choices=ESTADO)
    nota = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.producto.nombre
