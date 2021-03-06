# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-25 22:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0090_auto_20180925_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 25, 17, 24, 12, 287402), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 9, 25, 17, 24, 12, 289555), editable=False, max_length=1000, null=True),
        ),
    ]
