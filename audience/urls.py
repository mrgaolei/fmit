from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 'audience.views.index'),
	url(r'^auth_redirect/(?P<auth_type>\d*)$', 'audience.views.auth_redirect', name='auth_redirect'),
]
