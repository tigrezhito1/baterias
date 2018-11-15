# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-20 16:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_auto_20180911_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 11, 20, 3, 274943), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 9, 20, 11, 20, 3, 277673), editable=False, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='marca_producto',
            field=models.ForeignKey(blank=True, help_text='Marca de la bateria ', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_marca', to='app.Bateria'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='modelo_bateria',
            field=models.ForeignKey(blank=True, help_text='Modelo de la bateria', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_modelo', to='app.Bateria'),
        ),
    ]