# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-05 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20180304_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apeclasseswidget',
            name='class_type',
            field=models.CharField(blank=True, choices=[('IMPROV', 'Improv'), ('SKETCH', 'Sketch'), ('ACTING', 'Acting'), ('WORKSHOP', 'Workshop')], default='IMPROV', max_length=100, null=True),
        ),
    ]
