# coding=UTF-8
import hashlib
from urllib import urlretrieve

from django.core.files import File
from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField
import re


# Create your models here.

def strip_html(html):
    return re.sub(r'<.*?>', '', html)


class Source(models.Model):
    key = models.CharField(u"来源站ID", max_length=50, primary_key=True)
    name = models.CharField(u"网站名称", max_length=50)
    url = models.URLField(u"网址")
    active = models.BooleanField(u"抓取", default=True)
    running = models.BooleanField(u"抓取中", default=False)
    interval = models.DurationField(u"抓取间隔")
    url_list = models.URLField(u"列表地址")
    created = models.DateTimeField(u"创建时间", auto_now_add=True)
    updated = models.DateTimeField(u"更新时间", auto_now=True)
    re_list = models.TextField(u"列表正则")
    renum_newsid = models.SmallIntegerField(u"正则结果：来源站文章ID", default=0)
    renum_url = models.SmallIntegerField(u"正则结果：URL", default=1)
    reopt_url_isrelative = models.BooleanField(u"正则选项：URL", default=True, help_text=u"选中后，正则匹配的URL前会加上站点网址")
    renum_title = models.SmallIntegerField(u"正则结果：标题", default=2)
    renum_thumb = models.SmallIntegerField(u"正则结果：缩略图", default=5)
    renum_introduce = models.SmallIntegerField(u"正则结果：简介", default=6)
    renum_pubdate = models.SmallIntegerField(u"正则结果：文章时间", default=4)
    renum_publisher = models.SmallIntegerField(u"正则结果：撰稿人", default=3)
    re_content = models.TextField(u"内容正则")

    def __unicode__(self):
        return self.name

    def sync(self):
        import httplib2
        if not self.active and self.running:
            return 0
        self.running = True
        self.save()
        h = httplib2.Http()
        resp, content = h.request(self.url_list)
        # print resp, content
        if resp['status'] == '200':
            pass
        items = re.findall(str(self.re_list), content, re.DOTALL)
        total = 0
        for item in items:
            try:
                News.objects.get(source=self, newsid=item[self.renum_newsid])
                continue
            except News.DoesNotExist:
                pass
            news = News()
            news.source = self
            news.newsid = item[self.renum_newsid]
            if self.reopt_url_isrelative:
                news.url = self.url + item[self.renum_url]
            else:
                news.url = item[self.renum_url]
            news.title = strip_html(item[self.renum_title])
            news.thumb_url = item[self.renum_thumb]
            news.introduce = strip_html(item[self.renum_introduce])
            news.pubdate = item[self.renum_pubdate]
            news.publisher = item[self.renum_publisher]
            # store thumb
            if news.thumb_url:
                try:
                    result = urlretrieve(news.thumb_url)
                    file_ext = result[0].split('.')[1]
                    file = open(result[0], 'rb')
                    news.thumb.save('%s.%s' % (hashlib.md5(file.read()).hexdigest(), file_ext),
                                    File(file))
                except IOError:
                    pass
            news.save()

            # fetch content
            resp, content = h.request(news.url)
            match = re.search(self.re_content, content, re.DOTALL)
            if match:
                content = Content()
                content.news = news
                content.content = match.groups()[0]
                content.save()

            total += 1
        self.running = False
        self.updated = timezone.localtime(timezone.now())
        self.save()
        return total

    class Meta:
        verbose_name = u"数据来源"
        verbose_name_plural = verbose_name


class News(models.Model):
    source = models.ForeignKey(Source, verbose_name=u"来源站")
    newsid = models.IntegerField(u"来源站文章ID")
    url = models.URLField(u"原文URL")
    title = models.CharField(u"标题", max_length=250, db_index=True)
    thumb = models.ImageField(u"封面图", upload_to="news_thumb")
    thumb_url = models.URLField(u"封面图URL")
    introduce = models.CharField(u"简介", max_length=250)
    pubdate = models.DateTimeField(u"新闻时间", db_index=True)
    publisher = models.CharField(u"撰稿人", max_length=100)
    created = models.DateTimeField(u"创建时间", auto_now_add=True)
    updated = models.DateTimeField(u"更新时间", auto_now=True)
    support = models.IntegerField(u"支持数", default=0)
    oppose = models.IntegerField(u"反对数", default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"新闻"
        verbose_name_plural = verbose_name
        ordering = ['-pubdate']
        unique_together = (("source", "newsid"),)


class Content(models.Model):
    news = models.OneToOneField(News, verbose_name=u"新闻")
    content = HTMLField(u"文章内容")

    def __unicode__(self):
        return self.news.title

    class Meta:
        verbose_name = u"新闻内容"
        verbose_name_plural = verbose_name


class MacSkill(models.Model):
    subject = models.CharField(u"技巧标题", max_length=200)
    cmd = models.CharField(u"Command Line", max_length=255, blank=True)
    url = models.URLField(u"来源", blank=True)

    class Meta:
        verbose_name = u"mac技巧"


class MacSkillContent(models.Model):
    mac_skill = models.OneToOneField(MacSkill)
    content = HTMLField(u"技巧内容")


class Volume(models.Model):
    VOLUME_STATUS_COLLECT = 0
    VOLUME_STATUS_RECORD = 1
    VOLUME_STATUS_RELEASE = 2
    VOLUME_STATUS = (
        (VOLUME_STATUS_COLLECT, u"话题征集中"),
        (VOLUME_STATUS_RECORD, u"正在录音"),
        (VOLUME_STATUS_RELEASE, u"已发布"),
    )
    vol = models.IntegerField(u"期")
    subject = models.CharField(u"节目标题", max_length=200)
    status = models.SmallIntegerField(u"状态", choices=VOLUME_STATUS, default=VOLUME_STATUS_COLLECT, db_index=True)
    collect = models.CharField(u"征集文", max_length=255)
    mac_skill = models.ForeignKey(MacSkill)
    digi_rec = None
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "FMiT.VOL%d %s" % (self.vol, self.subject)

    class Meta:
        verbose_name = u"节目"
        ordering = ['-vol']


class Information(models.Model):
    volume = models.ForeignKey(Volume)
    subject = models.CharField(u"新闻标题", max_length=200)
    news = models.ForeignKey(News, blank=True, null=True)

    def __unicode__(self):
        return self.volume
