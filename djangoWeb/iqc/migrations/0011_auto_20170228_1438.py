# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-28 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iqc', '0010_delete_iqcdatacvte6486'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iqcdatacvte6486copy',
            options={'permissions': (('search_IQCDataCVTE6486COPY', 'can see data'), ('upload_IQCDataCVTE6486COPY', 'can upload data'))},
        ),
    ]
