from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('category/<slug:slug>/', ArticleListView.as_view(), name='category_articles'),
    path('author/<str:username>/', ArticleListView.as_view(), name='author_articles'),  

]