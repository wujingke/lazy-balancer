# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0003_auto_20160712_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy_config',
            name='ssl_cert',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='proxy_config',
            name='ssl_key',
            field=models.CharField(max_length=32, null=True),
        ),
    ]