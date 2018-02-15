# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='videos',
            field=models.ManyToManyField(blank=True, to='pages.VideoWidget'),
        ),
    ]
