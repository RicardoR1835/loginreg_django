# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-22 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_auto_20190522_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comments',
        ),
    ]
