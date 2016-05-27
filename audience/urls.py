from django.conf.urls import include, url
from audience import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^auth_redirect/(?P<auth_type>\d*)$', views.auth_redirect, name='auth_redirect'),
]
