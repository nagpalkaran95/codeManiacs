# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 12:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0008_auto_20170507_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemset',
            name='publishDate',
            field=models.DateField(default=datetime.date(2017, 5, 7)),
        ),
    ]
