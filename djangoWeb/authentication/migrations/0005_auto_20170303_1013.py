# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-03 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20170303_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='id_number',
            new_name='id_num',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='telephone_number',
            new_name='telephone_num',
        ),
    ]
