# Generated by Django 5.1.6 on 2025-03-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_pagina', '0009_rename_tipo_producto_tipo_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
