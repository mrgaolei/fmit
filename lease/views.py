# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView

from lease.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'lease/home.html', {
        'products': products
    })


class ProductDetail(DetailView):
    model = Product
