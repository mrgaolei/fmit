from django.conf.urls import include, url
from news import views

urlpatterns = [
    url(r'^p/(?P<page>\d*)/$', views.news_list, name='news_list_page'),
    url(r'^(?P<id>\d*)\.html$', views.news_detail, name='news_detail'),
]
