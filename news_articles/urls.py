from django.urls import path

from news_articles import views

urlpatterns = [
    path('', views.NewsArticleListView.as_view(), name="news_articles"),
    path(r'<int:pk>/', views.NewsArticleDetailView.as_view(), name="news_article"),
]
