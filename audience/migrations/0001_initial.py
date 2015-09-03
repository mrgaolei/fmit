# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('third', models.SmallIntegerField(default=1, verbose_name='\u8ba4\u8bc1\u7c7b\u578b', choices=[(1, '\u5fae\u535a'), (2, '\u5fae\u4fe1')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6863\u6848',
                'verbose_name_plural': '\u7528\u6237\u6863\u6848',
            },
        ),
        migrations.CreateModel(
            name='ThirdAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_type', models.SmallIntegerField(default=1, verbose_name='\u8ba4\u8bc1\u7c7b\u578b', choices=[(1, '\u5fae\u535a'), (2, '\u5fae\u4fe1')])),
                ('screen_name', models.CharField(max_length=255, verbose_name='\u6635\u79f0')),
                ('access_token', models.CharField(max_length=255, verbose_name=b'access_token')),
                ('expires_in', models.DateTimeField(verbose_name='token\u8fc7\u671f')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(verbose_name='\u7528\u6237\u6863\u6848', to='audience.Profile')),
            ],
            options={
                'verbose_name': '\u7b2c\u4e09\u65b9\u8ba4\u8bc1',
                'verbose_name_plural': '\u7b2c\u4e09\u65b9\u8ba4\u8bc1',
            },
        ),
        migrations.AlterUniqueTogether(
            name='thirdauth',
            unique_together=set([('profile', 'auth_type')]),
        ),
    ]
