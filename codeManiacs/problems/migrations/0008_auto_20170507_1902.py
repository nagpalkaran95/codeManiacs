# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0007_auto_20170507_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemset',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
