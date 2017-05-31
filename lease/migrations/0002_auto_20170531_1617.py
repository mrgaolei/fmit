# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='in_use',
            field=models.BooleanField(db_index=True, default=False, editable=False, verbose_name='\u4f7f\u7528\u4e2d'),
        ),
        migrations.AlterField(
            model_name='shipaddress',
            name='postcode',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
