# Generated by Django 2.2.6 on 2020-03-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0004_auto_20200301_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='nota',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
