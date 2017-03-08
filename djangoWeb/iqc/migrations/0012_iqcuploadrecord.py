# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 15:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iqc', '0011_auto_20170228_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='IQCUploadRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_num', models.DateTimeField(verbose_name='上传数量')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_upload_record', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]