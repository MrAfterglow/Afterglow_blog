# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-14 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0009_auto_20180814_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='r_u',
        ),
        migrations.AddField(
            model_name='role',
            name='r_u',
            field=models.ManyToManyField(to='backweb.User'),
        ),
    ]
