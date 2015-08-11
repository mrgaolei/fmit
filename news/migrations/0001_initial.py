# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('newsid', models.IntegerField(verbose_name='\u6765\u6e90\u7ad9\u6587\u7ae0ID')),
                ('url', models.URLField(verbose_name='\u539f\u6587URL')),
                ('title', models.CharField(max_length=250, verbose_name='\u6807\u9898', db_index=True)),
                ('thumb', models.ImageField(upload_to=b'news_thumb', verbose_name='\u5c01\u9762\u56fe')),
                ('thumb_url', models.URLField(verbose_name='\u5c01\u9762\u56feURL')),
                ('introduce', models.CharField(max_length=250, verbose_name='\u7b80\u4ecb')),
                ('pubdate', models.DateTimeField(verbose_name='\u65b0\u95fb\u65f6\u95f4', db_index=True)),
                ('publisher', models.CharField(max_length=100, verbose_name='\u64b0\u7a3f\u4eba')),
                ('content', tinymce.models.HTMLField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('support', models.IntegerField(default=0, verbose_name='\u652f\u6301\u6570')),
                ('oppose', models.IntegerField(default=0, verbose_name='\u53cd\u5bf9\u6570')),
            ],
            options={
                'ordering': ['-pubdate'],
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('key', models.CharField(max_length=50, serialize=False, verbose_name='\u6765\u6e90\u7ad9ID', primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u7f51\u7ad9\u540d\u79f0')),
                ('url', models.URLField(verbose_name='\u7f51\u5740')),
                ('active', models.BooleanField(default=True, verbose_name='\u6293\u53d6')),
                ('running', models.BooleanField(default=False, verbose_name='\u6293\u53d6\u4e2d')),
                ('interval', models.DurationField(verbose_name='\u6293\u53d6\u95f4\u9694')),
                ('url_list', models.URLField(verbose_name='\u5217\u8868\u5730\u5740')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('re_list', models.TextField(verbose_name='\u5217\u8868\u6b63\u5219')),
                ('renum_newsid', models.SmallIntegerField(default=0, verbose_name='\u6b63\u5219\u7ed3\u679c\uff1a\u6765\u6e90\u7ad9\u6587\u7ae0ID')),
                ('renum_url', models.SmallIntegerField(default=1, verbose_name='\u6b63\u5219\u7ed3\u679c\uff1aURL')),
                ('reopt_url_isrelative', models.BooleanField(default=True, help_text='\u9009\u4e2d\u540e\uff0c\u6b63\u5219\u5339\u914d\u7684URL\u524d\u4f1a\u52a0\u4e0a\u7ad9\u70b9\u7f51\u5740', verbose_name='\u6b63\u5219\u9009\u9879\uff1aURL')),
                ('renum_title', models.SmallIntegerField(default=2, verbose_name='\u6b63\u5219\u7ed3\u679c\uff1a\u6807\u9898')),
                ('renum_thumb', models.SmallIntegerField(default=5, verbose_name='\u6b63\u5219\u7ed3\u679c\uff1a\u7f29\u7565\u56fe')),
                ('renum_introduce', models.SmallIntegerField(default=6, verbose_name='\u6b63\u5219\u7ed3\u679c\uff1a\u7b80\u4ecb')),
                ('renum_pubdate', models.SmallIntegerField(default=4, verbose_name='\u6b63\u5219\u7ed3\u679c\uff1a\u6587\u7ae0\u65f6\u95f4')),
                ('renum_publisher', models.SmallIntegerField(default=3, verbose_name='\u6b63\u5219\u7ed3\u679c\uff1a\u64b0\u7a3f\u4eba')),
                ('re_content', models.TextField(verbose_name='\u5185\u5bb9\u6b63\u5219')),
            ],
            options={
                'verbose_name': '\u6570\u636e\u6765\u6e90',
                'verbose_name_plural': '\u6570\u636e\u6765\u6e90',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.ForeignKey(verbose_name='\u6765\u6e90\u7ad9', to='news.Source'),
        ),
        migrations.AlterUniqueTogether(
            name='news',
            unique_together=set([('source', 'newsid')]),
        ),
    ]
