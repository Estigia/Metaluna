# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 22:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Transacciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura',
            options={'ordering': ['-fecha']},
        ),
        migrations.AddField(
            model_name='factura',
            name='fecha',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 7, 31, 22, 59, 18, 242074, tzinfo=utc)),
            preserve_default=False,
        ),
    ]