# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-18 12:44
from __future__ import unicode_literals

import DjangoUeditor3.DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0012_article_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor3.DjangoUeditor.models.UEditorField(default=True),
        ),
    ]
