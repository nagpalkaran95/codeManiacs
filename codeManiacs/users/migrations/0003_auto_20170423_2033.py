# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170411_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='probAttemped',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='probSolved',
            field=models.CharField(default='', max_length=20000),
        ),
    ]
