# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0019_auto_20170514_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='acceptedAns',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='forum',
            name='solved',
            field=models.IntegerField(default=0),
        ),
    ]
