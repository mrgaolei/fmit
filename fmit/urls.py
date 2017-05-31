"""fmit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from rest_framework import routers

from news import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'volume', views.VolumeViewSet)


urlpatterns = [
    url(r'^$', views.home),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^working-mac/(?P<slug>.*)/$', views.MacSkillDetail.as_view(), name='working-mac'),
    url(r'^audience/', include('audience.urls', namespace='audience')),
    url(r'^zu/', include('lease.urls', namespace='lease')),

    url(r'^comments/', include('django_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
