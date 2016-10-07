# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0001_initial'),
        ('Agencia', '0002_auto_20160725_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sueldo', models.FloatField(blank=True, null=True)),
                ('horasExtra', models.FloatField(blank=True, null=True)),
                ('bonoIncentivo', models.FloatField(blank=True, null=True)),
                ('igss', models.FloatField(blank=True, null=True)),
                ('isr', models.FloatField(blank=True, null=True)),
                ('anticipos', models.FloatField(blank=True, null=True)),
                ('judiciales', models.FloatField(blank=True, null=True)),
                ('otros', models.FloatField(blank=True, null=True)),
                ('totalDescuento', models.FloatField(blank=True, null=True)),
                ('totalLiquido', models.FloatField(blank=True, null=True)),
                ('Agencia_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Agencia.Agencia')),
                ('Empleado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Empleado')),
            ],
        ),
    ]
