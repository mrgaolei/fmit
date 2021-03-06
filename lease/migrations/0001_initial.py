# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 13:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, verbose_name='Slug')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='\u5206\u7c7b')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u5206\u7c7b',
                'verbose_name_plural': '\u5546\u54c1\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.BigIntegerField(editable=False, unique=True, verbose_name='\u8ba2\u5355\u7f16\u53f7')),
                ('status', models.SmallIntegerField(choices=[(0, '\u5df2\u53d6\u6d88'), (1, '\u65b0\u8ba2\u5355'), (10, '\u5df2\u652f\u4ed8\u62bc\u91d1'), (20, '\u5df2\u5bc4\u51fa'), (30, '\u5f00\u59cb\u8bd5\u7528'), (40, '\u5bc4\u56de\u9014\u4e2d'), (50, '\u5df2\u5f52\u8fd8'), (60, '\u5df2\u5b8c\u6210')], db_index=True, default=1, verbose_name='\u72b6\u6001')),
                ('payables', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u5e94\u4ed8')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='\u5b9e\u4ed8')),
                ('tracking_forward', models.SlugField(blank=True, verbose_name='\u5bc4\u51fa\u8fd0\u5355\u53f7')),
                ('tracking_backward', models.SlugField(blank=True, verbose_name='\u5bc4\u56de\u8fd0\u5355\u53f7')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
                'permissions': (('can_test_order', '\u5185\u6d4b\u7528\u6237'),),
            },
        ),
        migrations.CreateModel(
            name='OrderLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, '\u5df2\u53d6\u6d88'), (1, '\u65b0\u8ba2\u5355'), (10, '\u5df2\u652f\u4ed8\u62bc\u91d1'), (20, '\u5df2\u5bc4\u51fa'), (30, '\u5f00\u59cb\u8bd5\u7528'), (40, '\u5bc4\u56de\u9014\u4e2d'), (50, '\u5df2\u5f52\u8fd8'), (60, '\u5df2\u5b8c\u6210')], verbose_name='\u72b6\u6001')),
                ('msg', models.CharField(blank=True, max_length=200, verbose_name='\u4fe1\u606f')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='lease.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, verbose_name='Slug')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('official_web', models.URLField(blank=True, verbose_name='\u5b98\u7f51')),
                ('picture', models.ImageField(upload_to='lease_product', verbose_name='\u56fe\u7247')),
                ('origin_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u539f\u4ef7')),
                ('pledge_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u62bc\u91d1')),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u65e5\u79df\u91d1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='lease.Category')),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', tinymce.models.HTMLField(verbose_name='\u5546\u54c1\u63cf\u8ff0')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='lease.Product')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u63cf\u8ff0',
                'verbose_name_plural': '\u5546\u54c1\u63cf\u8ff0',
            },
        ),
        migrations.CreateModel(
            name='ShipAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('province', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('district', models.CharField(blank=True, max_length=120)),
                ('address', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=20)),
                ('tel', models.CharField(blank=True, max_length=40)),
                ('mobile', models.CharField(blank=True, max_length=11)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ship_address', to='lease.Order')),
            ],
            options={
                'verbose_name': '\u6536\u8d27\u5730\u5740',
                'verbose_name_plural': '\u6536\u8d27\u5730\u5740',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=100, verbose_name='\u5e8f\u5217\u53f7')),
                ('fineness', models.SmallIntegerField(choices=[(100, '\u5168\u65b0'), (99, '99\u65b0')], db_index=True, default=99, verbose_name='\u6210\u8272')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='lease.Product')),
            ],
            options={
                'verbose_name': '\u5e93\u5b58',
                'verbose_name_plural': '\u5e93\u5b58',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='lease.Stock'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set([('product', 'sn')]),
        ),
    ]
