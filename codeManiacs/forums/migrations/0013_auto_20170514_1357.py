# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 13:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0012_remove_forum_anscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='-date'),
        ),
    ]
