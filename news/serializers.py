# coding=UTF-8
from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = News
		fields = ('id', 'newsid', 'title', 'thumb_url', 'introduce', 'pubdate', 'support', 'oppose',)