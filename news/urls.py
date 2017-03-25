from django.conf.urls import include, url
from news import views
from news.views import VolumeAutocomplete

urlpatterns = [
    url(r'^p/(?P<page>\d*)/$', views.news_list, name='news_list_page'),
    url(r'^(?P<id>\d*)\.html$', views.news_detail, name='news_detail'),
    url(r'^volume-autocomplete/$', VolumeAutocomplete.as_view(), name='volume-autocomplete'),
]
