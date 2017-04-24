# coding=UTF-8
from django.utils import timezone
from django_comments.models import Comment
from rest_framework import serializers

from .models import News, Volume


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'newsid', 'title', 'thumb_url', 'introduce', 'pubdate', 'support', 'oppose',)


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ('id', '__unicode__', 'vol', 'subject', 'status', 'category', 'album', 'created', 'updated')


class CommentSerializer(serializers.ModelSerializer):
    submit_date = timezone.now()
    ip_public = "True"
    is_removed = "False"

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('submit_date', 'is_public', 'is_removed', 'ip_address')
