# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-25 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180222_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apeclasseswidget',
            name='class_type',
            field=models.CharField(blank=True, choices=[('IMPROV', 'Improv'), ('SKETCH', 'Sketch'), ('ACTING', 'Acting'), ('WORKSHOP', 'Workshop')], default='gallery', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, choices=[('home', 'Home'), ('classes', 'Classes'), ('shows', 'Shows'), ('faculty', 'Faculty'), ('talent', 'Talent'), ('watch', 'Watch')], null=True),
        ),
    ]
