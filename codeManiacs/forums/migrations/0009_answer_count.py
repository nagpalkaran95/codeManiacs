# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0008_auto_20170508_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]