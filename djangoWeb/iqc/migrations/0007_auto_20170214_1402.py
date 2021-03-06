# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iqc', '0006_auto_20170214_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iqcdatacvte6486',
            name='cssj',
            field=models.DateTimeField(verbose_name='测试时间'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486',
            name='gwmc',
            field=models.CharField(max_length=100, verbose_name='工位名称'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486',
            name='pzxxbh',
            field=models.CharField(max_length=100, verbose_name='品质现象编号'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486',
            name='pzxxmc',
            field=models.CharField(max_length=100, verbose_name='品质现象名称'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486',
            name='scpc',
            field=models.CharField(max_length=100, verbose_name='生成批次'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486',
            name='tm',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='条码'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486copy',
            name='cssj',
            field=models.DateTimeField(verbose_name='测试时间'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486copy',
            name='gwmc',
            field=models.CharField(max_length=100, verbose_name='工位名称'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486copy',
            name='pzxxbh',
            field=models.CharField(max_length=100, verbose_name='品质现象编号'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486copy',
            name='pzxxmc',
            field=models.CharField(max_length=100, verbose_name='品质现象名称'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486copy',
            name='scpc',
            field=models.CharField(max_length=100, verbose_name='生成批次'),
        ),
        migrations.AlterField(
            model_name='iqcdatacvte6486copy',
            name='tm',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='条码'),
        ),
    ]
