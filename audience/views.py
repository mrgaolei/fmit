# coding=UTF-8
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import redirect
from django.shortcuts import render
from weibo import APIClient, APIError
from .models import THIRDAUTH_CHOICES, WEIBO, WEIXIN


def _create_client(request):
    return APIClient(3029223458,
                     '9183d1ae117f5cf5a2d03d029fe1f0c1',
                     request.build_absolute_uri(reverse('audience:auth_callback', args=(WEIBO,))))


# Create your views here.
def index(request):
    print request.user
    return render(request, 'audience/index.html', {'third_auth': THIRDAUTH_CHOICES})


def auth_redirect(request, auth_type):
    if int(auth_type) == WEIBO:
        client = _create_client(request)
    elif int(auth_type) == WEIXIN:
        raise Exception()
    return redirect(client.get_authorize_url())


def auth_callback(request, auth_type):
    if int(auth_type) == WEIBO:
        user = cb_weibo(request)
    elif int(auth_type) == WEIXIN:
        user = cb_weixin(request)
    else:
        user = None
    login(request, user)
    return redirect(reverse('news:news_list_page', args=(1,)))


@transaction.atomic()
def cb_weibo(request):
    code = request.GET['code']
    client = _create_client(request)
    try:
        r = client.request_access_token(code)
    except APIError:
        return redirect(reverse('audience:home'))
    access_token, expires_in, uid = r.access_token, r.expires_in, r.uid
    client.set_access_token(access_token, expires_in)
    u = client.users.show.get(uid=uid)
    user = authenticate(auth_type=WEIBO, auth_uid=uid, access_token=access_token,
                        screen_name=u.screen_name, expires_in=datetime.fromtimestamp(expires_in))
    return user


def cb_weixin(request):
    return ""
