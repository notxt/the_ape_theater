# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 21:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180215_0901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_time']},
        ),
    ]