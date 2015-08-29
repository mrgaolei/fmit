from django.conf.urls import include, url

urlpatterns = [
	url(r'^p/(?P<page>\d*)/$', 'news.views.news_list', name='news_list_page'),
    url(r'^(?P<id>\d*)\.html$', 'news.views.news_detail', name='news_detail'),
]
