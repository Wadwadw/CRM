from django.urls import path
from .views import NewsListView, NewsDetailView, NewsListApi


app_name = 'news'


urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/detail-news/', NewsDetailView.as_view(), name='news-detail'),
    path('api-news/', NewsListApi.as_view())
]