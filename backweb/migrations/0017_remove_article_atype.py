# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-06 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0016_auto_20180906_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='atype',
        ),
    ]
