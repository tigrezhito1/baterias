# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-04 17:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0138_auto_20181004_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 12, 25, 19, 474779), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 4, 12, 25, 19, 478439), editable=False, max_length=1000, null=True),
        ),
    ]
