# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agencia', '__first__'),
        ('Planillas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planilla',
            name='Agencia_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Agencia.Agencia'),
        ),
    ]
