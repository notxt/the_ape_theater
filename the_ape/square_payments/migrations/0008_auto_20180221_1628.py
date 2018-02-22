# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-22 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('square_payments', '0007_auto_20180220_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squarecustomer',
            name='profile',
        ),
        migrations.AddField(
            model_name='squarecustomer',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='squarecustomer',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='squarecustomer',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
