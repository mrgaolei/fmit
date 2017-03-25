# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-03-25 08:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='macskill',
            options={'verbose_name': 'mac\u6280\u5de7', 'verbose_name_plural': 'mac\u6280\u5de7'},
        ),
        migrations.AddField(
            model_name='macskill',
            name='author',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
