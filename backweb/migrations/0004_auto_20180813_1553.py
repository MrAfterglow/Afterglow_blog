# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0003_article_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.ImageField(upload_to='upload'),
        ),
    ]