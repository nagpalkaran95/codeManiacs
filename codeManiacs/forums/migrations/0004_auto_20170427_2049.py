# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-27 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_auto_20170427_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='forum',
            name='tags',
            field=models.CharField(default='', max_length=100),
        ),
    ]