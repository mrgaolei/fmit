# coding=UTF-8
from django.contrib import admin
from .models import Source, MacSkill, MacSkillContent
from .models import News
from .models import Content
from .models import Volume


# Register your models here.

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'active', 'running', 'interval', 'created', 'updated')
    readonly_fields = ['running']
    actions = ['make_sync']

    def make_sync(self, request, queryset):
        total = 0
        for source in queryset:
            total += source.sync()
        self.message_user(request, u"同步 %d 条新闻" % total)

    make_sync.short_description = u"同步新闻"


class ContentInline(admin.StackedInline):
    model = Content
    can_delete = False


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'newsid', 'pubdate', 'created', 'updated')
    list_filter = ['source', ]
    inlines = [ContentInline, ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['source', 'newsid']
        else:
            return []


class MacSkillContentInline(admin.StackedInline):
    model = MacSkillContent


@admin.register(MacSkill)
class MacSkillAdmin(admin.ModelAdmin):
    list_display = ('subject', 'volume')
    inlines = [MacSkillContentInline]


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_filter = ['status', 'category']
