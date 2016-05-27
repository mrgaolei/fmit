# coding=UTF-8
from django.core.urlresolvers import reverse
from weibo import APIClient
from django.shortcuts import render
from django.shortcuts import redirect
from .models import THIRDAUTH_CHOICES, WEIBO, WEIXIN


def _create_client(request):
    return APIClient(3029223458,
                     '9183d1ae117f5cf5a2d03d029fe1f0c1',
                     request.build_absolute_uri(reverse('audience:auth_callback', args=(WEIBO,))))


# Create your views here.
def index(request):
    return render(request, 'audience/index.html', {'third_auth': THIRDAUTH_CHOICES})


def auth_redirect(request, auth_type):
    if int(auth_type) == WEIBO:
        client = _create_client(request)
    elif int(auth_type) == WEIXIN:
        raise Exception()
    return redirect(client.get_authorize_url())


def auth_callback(request, auth_type):
    if int(auth_type) == WEIBO:
        return cb_weibo(request)
    elif int(auth_type) == WEIXIN:
        return cb_weixin(request)
    else:
        return None


def cb_weibo(request):
    return


def cb_weixin(request):
    return
