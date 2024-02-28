# news/urls.py
from django.urls import path
from .views import post_news, view_news, list_news

urlpatterns = [
    path('post/', post_news, name='post_news'),
    path('<int:news_id>/', view_news, name='view_news'),
    path('list/', list_news, name='news_list'),
]
