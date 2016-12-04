# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb\u5185\u5bb9',
                'verbose_name_plural': '\u65b0\u95fb\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='\u65b0\u95fb\u6807\u9898')),
            ],
        ),
        migrations.CreateModel(
            name='MacSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='\u6280\u5de7\u6807\u9898')),
                ('cmd', models.CharField(blank=True, max_length=255, verbose_name='Command Line')),
                ('url', models.URLField(blank=True, verbose_name='\u6765\u6e90')),
            ],
            options={
                'verbose_name': 'mac\u6280\u5de7',
            },
        ),
        migrations.CreateModel(
            name='MacSkillContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(verbose_name='\u6280\u5de7\u5185\u5bb9')),
                ('mac_skill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.MacSkill')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsid', models.IntegerField(verbose_name='\u6765\u6e90\u7ad9\u6587\u7ae0ID')),
                ('url', models.URLField(verbose_name='\u539f\u6587URL')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='\u6807\u9898')),
                ('thumb', models.ImageField(upload_to=b'news_thumb', verbose_name='\u5c01\u9762\u56fe')),
                ('thumb_url', models.URLField(verbose_name='\u5c01\u9762\u56feURL')),
                ('introduce', models.CharField(max_length=250, verbose_name='\u7b80\u4ecb')),
                ('pubdate', models.DateTimeField(db_index=True, verbose_name='\u65b0\u95fb\u65f6\u95f4')),
                ('publisher', models.CharField(max_length=100, verbose_name='\u64b0\u7a3f\u4eba')),
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
                ('key', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='\u6765\u6e90\u7ad9ID')),
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
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vol', models.IntegerField(verbose_name='\u671f')),
                ('subject', models.CharField(max_length=200, verbose_name='\u8282\u76ee\u6807\u9898')),
                ('status', models.SmallIntegerField(choices=[(0, '\u8bdd\u9898\u5f81\u96c6\u4e2d'), (1, '\u6b63\u5728\u5f55\u97f3'), (2, '\u5df2\u53d1\u5e03')], db_index=True, default=0, verbose_name='\u72b6\u6001')),
                ('collect', models.CharField(max_length=255, verbose_name='\u5f81\u96c6\u6587')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('mac_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.MacSkill')),
            ],
            options={
                'ordering': ['-vol'],
                'verbose_name': '\u8282\u76ee',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Source', verbose_name='\u6765\u6e90\u7ad9'),
        ),
        migrations.AddField(
            model_name='information',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
        migrations.AddField(
            model_name='information',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Volume'),
        ),
        migrations.AddField(
            model_name='content',
            name='news',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='\u65b0\u95fb'),
        ),
        migrations.AlterUniqueTogether(
            name='news',
            unique_together=set([('source', 'newsid')]),
        ),
    ]
