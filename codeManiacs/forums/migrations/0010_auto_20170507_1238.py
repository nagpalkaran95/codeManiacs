# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0009_auto_20170507_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='dateAnswered',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
