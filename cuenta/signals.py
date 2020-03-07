from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Cliente


def perfilCliente(sender, instance, created, **kwargs):
    if created:
        grupo = Group.objects.get(name='Cliente')

        instance.groups.add(grupo)
        Cliente.objects.create(usuario=instance, nombre=instance.username)


post_save.connect(perfilCliente, sender=User)
