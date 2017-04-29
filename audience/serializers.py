from django.contrib.auth.models import User
from rest_framework import serializers

from audience.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'last_login', 'groups', 'user_permissions', 'date_joined')
        read_only_fields = ('is_active', 'date_joined', 'username', 'first_name', 'last_name', 'email')
