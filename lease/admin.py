# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from lease.models import Category, Product, ProductDetail, Stock, Order, ShipAddress


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ProductDetailAdmin(admin.StackedInline):
    model = ProductDetail


class StockAdmin(admin.TabularInline):
    model = Stock
    extra = 0
    can_delete = False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', '=slug')
    list_display = ('name', 'slug', 'category', 'origin_price', 'pledge_price', 'price_per_day')
    list_filter = ['category']
    date_hierarchy = 'updated'
    inlines = [StockAdmin, ProductDetailAdmin]

    def has_delete_permission(self, request, obj=None):
        return False


class AddressAdmin(admin.StackedInline):
    model = ShipAddress


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('sn', 'user', 'stock', 'status', 'payables', 'amount', 'created')
    list_filter = ['status']
    inlines = [AddressAdmin]

    def get_queryset(self, request):
        queryset = super(OrderAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields]
        if obj:
            return ['stock']
        else:
            return ['status']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
