# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-28 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planillas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finanzas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo', models.BooleanField(default=None)),
                ('monto', models.FloatField()),
            ],
        ),
    ]
