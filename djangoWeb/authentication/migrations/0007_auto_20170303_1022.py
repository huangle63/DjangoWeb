# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-03 10:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20170303_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='post_address',
            new_name='location',
        ),
    ]
