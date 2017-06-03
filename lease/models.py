# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    slug = models.SlugField(u"Slug", primary_key=True)
    name = models.CharField(u"分类", max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"商品分类"
        verbose_name_plural = verbose_name


class Product(models.Model):
    slug = models.SlugField(u"Slug", primary_key=True)
    name = models.CharField(u"商品名称", max_length=200, unique=True)
    official_web = models.URLField(u"官网", blank=True)
    picture = models.ImageField(u"图片", upload_to='lease_product')
    category = models.ForeignKey(Category, related_name='products')
    origin_price = models.DecimalField(u"原价", max_digits=10, decimal_places=2)
    pledge_price = models.DecimalField(u"押金", max_digits=10, decimal_places=2)
    price_per_day = models.DecimalField(u"日租金", max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"商品"
        verbose_name_plural = verbose_name


class ProductDetail(models.Model):
    product = models.OneToOneField(Product, related_name='detail')
    description = HTMLField(u"商品描述")

    def __unicode__(self):
        return self.product.name

    class Meta:
        verbose_name = u"商品描述"
        verbose_name_plural = verbose_name


class Stock(models.Model):
    STOCK_FINENESS_NEW = 100
    STOCK_FINENESS_99 = 99
    STOCK_FINENESS = (
        (STOCK_FINENESS_NEW, u"全新"),
        (STOCK_FINENESS_99, u"99新"),
    )
    product = models.ForeignKey(Product, related_name='stocks')
    attr = models.CharField(u"型号", max_length=100, blank=True, default='')
    sn = models.CharField(u"序列号", max_length=100)
    fineness = models.SmallIntegerField(u"成色", choices=STOCK_FINENESS, default=STOCK_FINENESS_99, db_index=True)
    in_use = models.BooleanField(u"使用中", default=False, editable=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s %s [%s]" % (self.attr, self.product.name, self.sn)

    class Meta:
        verbose_name = u"库存"
        verbose_name_plural = verbose_name
        unique_together = (('product', 'sn'), )


class BaseAddress(models.Model):
    name = models.CharField(max_length=120)
    # country = models.ForeignKey(Country, limit_choices_to={'available': True}, verbose_name=_("Country"))
    province = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    district = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20, blank=True)
    tel = models.CharField(max_length=40, blank=True)
    mobile = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def clean(self):
        if not self.tel and not self.mobile:
            raise ValidationError({
                'mobile': ValidationError(u"手机固话必须填写其一"),
            })

    class Meta:
        abstract = True


class Order(models.Model):
    ORDER_STATUS_CANCEL = 0
    ORDER_STATUS_NEW = 1
    ORDER_STATUS_PAID = 10
    ORDER_STATUS_SHIPPED = 20
    ORDER_STATUS_RECEIVED = 30
    ORDER_STATUS_RETURNING = 40
    ORDER_STATUS_RETURNED = 50
    ORDER_STATUS_FINISH = 60
    ORDER_STATUS = (
        (ORDER_STATUS_CANCEL, u"已取消"),
        (ORDER_STATUS_NEW, u"新订单"),
        (ORDER_STATUS_PAID, u"已支付押金"),
        (ORDER_STATUS_SHIPPED, u"已寄出"),
        (ORDER_STATUS_RECEIVED, u"开始试用"),
        (ORDER_STATUS_RETURNING, u"寄回途中"),
        (ORDER_STATUS_RETURNED, u"已归还"),
        (ORDER_STATUS_FINISH, u"已完成"),
    )
    sn = models.BigIntegerField(u"订单编号", editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', editable=False)
    stock = models.ForeignKey(Stock, related_name='orders')
    status = models.SmallIntegerField(u"状态", choices=ORDER_STATUS, default=ORDER_STATUS_NEW, db_index=True)
    payables = models.DecimalField(u"应付", max_digits=10, decimal_places=2)
    amount = models.DecimalField(u"实付", max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField(u"开始使用日")
    end_date = models.DateField(u"归还日")
    tracking_forward = models.SlugField(u"寄出运单号", blank=True)
    tracking_backward = models.SlugField(u"寄回运单号", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.sn)

    @staticmethod
    def generate_sn():
        import time
        import random
        t = time.localtime()
        y = t.tm_year - 2014
        d = 1000 - t.tm_yday
        s = 100000 - t.tm_hour * 60 * 60 - t.tm_min * 60 - t.tm_sec
        r = random.randint(0, 99)

        n = y * 10000000000 + d * 10000000 + s * 100 + r
        return n

    def save(self, *args, **kwargs):
        if not self.sn:
            self.sn = Order.generate_sn()
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name
        permissions = (("can_test_order", u"内测用户"),)


class ShipAddress(BaseAddress):
    order = models.OneToOneField(Order, related_name='ship_address')

    class Meta:
        verbose_name = u"收货地址"
        verbose_name_plural = verbose_name


class OrderLog(models.Model):
    order = models.ForeignKey(Order, related_name='logs')
    operator = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.SmallIntegerField(u"状态", choices=Order.ORDER_STATUS)
    msg = models.CharField(u"信息", max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
