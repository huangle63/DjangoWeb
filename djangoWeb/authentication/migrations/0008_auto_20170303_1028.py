# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-03 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20170303_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='mobile',
            new_name='mobile_num',
        ),
    ]
