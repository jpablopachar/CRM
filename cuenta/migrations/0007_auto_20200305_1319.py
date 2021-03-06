# Generated by Django 2.2.6 on 2020-03-05 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0006_cliente_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
