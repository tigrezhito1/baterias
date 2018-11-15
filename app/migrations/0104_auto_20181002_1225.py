# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-02 17:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0103_auto_20181002_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 12, 25, 33, 969457), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 2, 12, 25, 33, 971504), editable=False, max_length=1000, null=True),
        ),
    ]
