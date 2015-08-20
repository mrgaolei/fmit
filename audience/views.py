# coding=UTF-8
from weibo import APIClient
from django.shortcuts import render
from django.shortcuts import redirect
from .models import WEIBO, THIRDAUTH_CHOICES


def _create_client():
	return APIClient(3029223458, '9183d1ae117f5cf5a2d03d029fe1f0c1', 'http://fmit.cn/admin/fmcore/userext/wbcb/')

# Create your views here.
def index(request):
	return render(request, 'audience/index.html', {'third_auth': THIRDAUTH_CHOICES})

def auth_redirect(request, auth_type):
	if int(auth_type) == WEIBO:
		client = _create_client()
	return redirect(client.get_authorize_url())

def cb_weibo(request):
	return

def cb_weixin(request):
	return