# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-03 16:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0127_auto_20181003_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='color',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 11, 49, 52, 73454), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 3, 11, 49, 52, 75254), editable=False, max_length=1000, null=True),
        ),
    ]
