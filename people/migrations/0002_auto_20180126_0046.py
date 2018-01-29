# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20180126_0046'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performer',
            name='house_team',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='person_ptr',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='person_ptr',
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='person',
            name='house_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.HouseTeam'),
        ),
        migrations.AddField(
            model_name='person',
            name='performs',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='teaches',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Performer',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
