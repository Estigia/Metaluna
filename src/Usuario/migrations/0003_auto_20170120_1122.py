# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-20 17:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_auto_20161214_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ultima_conexion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='log_user',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
