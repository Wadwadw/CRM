from django.shortcuts import render
from django.views import generic
from .models import News
from .serializers import NewsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class NewsListView(generic.ListView):
    template_name = 'landing_page.html'
    context_object_name = 'news_list'
    queryset = News.objects.all().order_by('-id')


class NewsDetailView(generic.DetailView):
    template_name = 'news_detail.html'
    queryset = News.objects.all()
    context_object_name = 'news_detail'


class NewsListApi(APIView):
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)
