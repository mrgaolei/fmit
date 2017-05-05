# coding=UTF-8
from datetime import datetime

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import redirect
from django.shortcuts import render
from weibo import APIClient, APIError
from .models import THIRDAUTH_CHOICES, WEIBO, QQ


def _create_client(request):
    return APIClient(settings.WEIBO_APP_KEY,
                     settings.WEIBO_APPSECRET,
                     request.build_absolute_uri(reverse('audience:auth_callback', args=(WEIBO,))))


# Create your views here.
def index(request):
    print request.user
    return render(request, 'audience/index.html', {'third_auth': THIRDAUTH_CHOICES})


def auth_redirect(request, auth_type):
    if int(auth_type) == WEIBO:
        client = _create_client(request)
    elif int(auth_type) == QQ:
        raise Exception()
    return redirect(client.get_authorize_url())


def auth_callback(request, auth_type):
    if int(auth_type) == WEIBO:
        user = cb_weibo(request)
    elif int(auth_type) == QQ:
        user = cb_qq(request)
    else:
        user = None
    login(request, user)
    return redirect('/')


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
    print u
    user = authenticate(auth_type=WEIBO, auth_uid=uid, access_token=access_token,
                        screen_name=u.screen_name, avatar=u.avatar_large,
                        expires_in=datetime.fromtimestamp(expires_in))
    return user


def cb_qq(request):
    return ""
