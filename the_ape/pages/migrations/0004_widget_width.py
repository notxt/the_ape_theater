# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180225_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='width',
            field=models.CharField(choices=[('full', 'Full'), ('two_thirds', 'Two Thirds'), ('half', 'Half'), ('one_third', 'One Third')], default='full', max_length=100),
        ),
    ]
