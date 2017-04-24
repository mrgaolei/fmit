from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from dal import autocomplete
from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework.pagination import CursorPagination

from .models import News, Volume, MacSkill
from .serializers import NewsSerializer

# Create your views here.


def home(request):
    # coll
    vol_coll = Volume.objects.filter(status=Volume.VOLUME_STATUS_COLLECT)[:10]
    vol_release = Volume.objects.filter(status=Volume.VOLUME_STATUS_RELEASE)[:10]

    return render(request, 'news/home.html', {
        'vol_coll': vol_coll,
        'vol_release': vol_release,
    })


def news_list(request, page=1):
    list = News.objects.all()
    paginator = Paginator(list, 20)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'news/list.html', {'list': list})


def news_detail(request, id):
    news = News.objects.get(pk=id)
    return render(request, 'news/detail.html', {'news': news})


class MacSkillDetail(DetailView):
    model = MacSkill
    slug_field = 'brow'


# DAL


class VolumeAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Volume.objects.none()
        qs = Volume.objects.all()
        if self.q:
            try:
                vol_int = int(self.q)
                qs = qs.filter(vol=vol_int)
            except ValueError:
                qs = qs.filter(subject__contains=self.q)

        return qs


# DRF


class NewsResultsSetPagination(CursorPagination):
    ordering = '-pubdate'


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsResultsSetPagination
