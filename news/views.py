from django.shortcuts import render

from .models import News
# Create your views here.

def home(request):
	return news_list(request)

def news_list(request):
	list = News.objects.all()
	return render(request, 'news/list.html', {'list': list})

def news_detail(request, id):
	news = News.objects.get(pk=id)
	return render(request, 'news/detail.html', {'news': news})
