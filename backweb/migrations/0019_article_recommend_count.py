# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-07 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0018_auto_20180906_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='recommend_count',
            field=models.IntegerField(null=True),
        ),
    ]
