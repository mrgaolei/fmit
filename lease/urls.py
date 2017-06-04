from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='lease_home'),
    url(r'^(?P<slug>[a-z0-9\-]+)/$', views.ProductDetail.as_view(), name='lease_detail')
]
