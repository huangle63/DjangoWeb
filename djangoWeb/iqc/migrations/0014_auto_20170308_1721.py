# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-08 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iqc', '0013_auto_20170306_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iqcuploadrecord',
            options={'ordering': ['upload_time']},
        ),
    ]