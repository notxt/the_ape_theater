# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=100)),
                ('start_time', models.DateTimeField(null=True)),
                ('max_tickets', models.IntegerField(null=True)),
                ('tickets_sold', models.IntegerField(default=0)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]
