# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 15:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20180904_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 4, 15, 38, 7, 245875), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]
