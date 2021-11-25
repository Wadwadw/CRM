from django.shortcuts import render
from django.views import generic
from .models import News


class NewsListView(generic.ListView):
    template_name = 'landing_page.html'
    context_object_name = 'news_list'
    queryset = News.objects.all().order_by('-id')


class NewsDetailView(generic.DetailView):
    template_name = 'news_detail.html'
    queryset = News.objects.all()
    context_object_name = 'news_detail'

