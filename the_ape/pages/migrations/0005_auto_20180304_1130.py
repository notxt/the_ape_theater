# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-04 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_widget_width'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApeClassFocusWidget',
        ),
        migrations.DeleteModel(
            name='EventFocusWidget',
        ),
    ]
