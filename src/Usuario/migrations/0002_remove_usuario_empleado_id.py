# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 06:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Empleado_id',
        ),
    ]
