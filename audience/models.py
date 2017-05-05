# coding=UTF-8
from django.db import models
from django.conf import settings

# Create your models here.
WEIBO = 1
QQ = 2
THIRDAUTH_CHOICES = (
    (WEIBO, u'微博'),
    (QQ, u'QQ'),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u"用户")
    auth_type = models.SmallIntegerField(u"认证类型", choices=THIRDAUTH_CHOICES, default=WEIBO)
    auth_uid = models.BigIntegerField(u"第三方UID")
    screen_name = models.CharField(u"昵称", max_length=255)
    access_token = models.CharField("access_token", max_length=255)
    expires_in = models.DateTimeField(u"token过期")
    avatar_url = models.URLField(u"头像", blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.screen_name

    class Meta:
        verbose_name = u"用户档案"
        verbose_name_plural = verbose_name
        unique_together = (('auth_type', 'auth_uid'),)
