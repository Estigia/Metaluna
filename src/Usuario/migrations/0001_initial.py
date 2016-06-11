# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55, null=True)),
                ('apellidos', models.CharField(max_length=90, null=True)),
                ('cui', models.CharField(max_length=13, null=True)),
                ('nit', models.CharField(max_length=20, null=True)),
                ('sueldo', models.FloatField(null=True)),
                ('Agencia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.Agencia')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puesto', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ultima_conexion', models.DateTimeField(auto_now=True)),
                ('Empleado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Empleado')),
                ('Tipo_Usuario_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Usuario.Tipo_Usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='Puesto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Puesto'),
        ),
    ]