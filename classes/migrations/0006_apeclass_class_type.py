# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20180126_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='apeclass',
            name='class_type',
            field=models.CharField(choices=[('IMPROV', 'Improv'), ('SKETCH', 'Sketch'), ('ACTING', 'Acting')], default='IMPROV', max_length=50),
            preserve_default=False,
        ),
    ]
