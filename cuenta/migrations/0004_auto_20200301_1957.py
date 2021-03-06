# Generated by Django 2.2.6 on 2020-03-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0003_auto_20200301_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='etiquetas',
            field=models.ManyToManyField(to='cuenta.Etiqueta'),
        ),
    ]
