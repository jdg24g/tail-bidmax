# Generated by Django 5.1.6 on 2025-02-28 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_pagina', '0005_alter_ticket_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='celular',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
