# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibre',
            name='calibre',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
