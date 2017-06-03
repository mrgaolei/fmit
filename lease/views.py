# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from lease.models import Stock


def home(request):
    stocks = Stock.objects.select_related('product').all()
    return render(request, 'lease/home.html', {
        'stocks': stocks
    })
