# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyhandover', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gyhandover',
            name='handover_img',
            field=models.ImageField(upload_to='./image/gyhandover/%Y/%m', verbose_name='附件图片'),
        ),
    ]
