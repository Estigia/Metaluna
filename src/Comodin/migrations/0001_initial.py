# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comodin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, null=True)),
                ('empresa', models.CharField(max_length=45, null=True)),
                ('direccion', models.CharField(max_length=45, null=True)),
                ('telefono', models.CharField(max_length=8)),
                ('nit', models.CharField(max_length=20, null=True)),
                ('tipo', models.BooleanField(default=False)),
                ('bloqueado', models.BooleanField(default=False)),
                ('saldo', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=45)),
                ('Comodin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comodin.Comodin')),
            ],
        ),
    ]
