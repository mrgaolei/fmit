# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(blank=True, default=b'', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='auth_type',
            field=models.SmallIntegerField(choices=[(1, '\u5fae\u535a'), (2, 'QQ')], default=1, verbose_name='\u8ba4\u8bc1\u7c7b\u578b'),
        ),
    ]
