# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-01 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_houseteam_image_carousel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseteam',
            name='banner',
        ),
    ]
