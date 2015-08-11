from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 'news.views.news_list'),
    url(r'^(?P<id>\d*)\.html$', 'news.views.news_detail', name='news_detail'),
]
