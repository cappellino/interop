# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-08 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auvsi_suas', '0034_remove_moving_obstacle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missionconfig',
            name='is_active', ),
    ]
