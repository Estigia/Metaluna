# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mercaderia',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
