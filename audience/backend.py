import random

from audience.models import Profile
from django.contrib.auth.models import User
from django.db import IntegrityError


def create_user_by_username(username, email=None):
    try:
        user = User.objects.create_user(username, email)
    except IntegrityError:
        username += str(random.randint(10000, 99999))
        return create_user_by_username(username, email)
    return user


class ThirdAuthBackend(object):

    def authenticate(self, auth_type, auth_uid, access_token, screen_name, avatar=None, expires_in=None):
        try:
            profile = Profile.objects.get(auth_type=auth_type, auth_uid=auth_uid)
            user = profile.user
        except Profile.DoesNotExist:
            user = create_user_by_username(screen_name)
            profile = Profile(user=user, auth_type=auth_type, auth_uid=auth_uid, screen_name=screen_name)

        profile.access_token = access_token
        profile.avatar_url = avatar
        if expires_in:
            profile.expires_in = expires_in
        profile.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
