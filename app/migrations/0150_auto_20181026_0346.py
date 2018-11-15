# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-26 08:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0149_auto_20181023_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 26, 3, 46, 30, 43762), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
    ]
