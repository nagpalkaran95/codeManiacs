# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-27 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20170422_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemset',
            name='tags',
            field=models.CharField(default='', max_length=200),
        ),
    ]
