# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planillas', '0002_planilla_agencia_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilla',
            name='anticipos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='bonoIncentivo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='horasExtra',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='igss',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='isr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='judiciales',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='otros',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='sueldo',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='totalDescuento',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='totalLiquido',
            field=models.FloatField(blank=True, null=True),
        ),
    ]