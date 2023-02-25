from django.views.generic import ListView, DetailView

from news_articles.models import NewsArticle


# Create your views here.
class NewsArticleListView(ListView):
    model = NewsArticle
    queryset = NewsArticle.objects.filter(visible=True)
    template_name = "news.html"
    ordering = "-date"


class NewsArticleDetailView(DetailView):
    model = NewsArticle
    template_name = "news_article.html"
