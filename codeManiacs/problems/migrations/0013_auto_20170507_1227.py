# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0012_remove_problemset_publishdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemset',
            name='problemSetter',
        ),
        migrations.RemoveField(
            model_name='problemset',
            name='problemTester',
        ),
        migrations.RemoveField(
            model_name='problemset',
            name='timeLimit',
        ),
    ]
