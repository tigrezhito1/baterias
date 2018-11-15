# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-03 15:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0119_auto_20181003_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colores_v',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='produccion',
            name='color',
            field=models.ForeignKey(blank=True, help_text='Color', max_length=1000, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_nombre', to='app.Colores_v'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 10, 46, 15, 803212), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='hora_instalacion',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 10, 3, 10, 46, 15, 804153), editable=False, max_length=1000, null=True),
        ),
    ]
