# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0015_auto_20170514_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='acceptedAns',
            field=models.CharField(default='No', max_length=5),
        ),
        migrations.AlterField(
            model_name='forum',
            name='solved',
            field=models.CharField(default='No', max_length=5),
        ),
    ]
