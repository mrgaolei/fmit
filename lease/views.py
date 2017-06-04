# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from lease.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'lease/home.html', {
        'products': products
    })
