from django.conf.urls import include, url

urlpatterns = [
	url(r'^p/(?P<page>\d*)/$', 'news.views.news_list'),
    url(r'^(?P<id>\d*)\.html$', 'news.views.news_detail', name='news_detail'),
]
