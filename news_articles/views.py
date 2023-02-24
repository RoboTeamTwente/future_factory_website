from django.views.generic import ListView, DetailView

from news_articles.models import NewsArticle


# Create your views here.
class NewsArticleListView(ListView):
    model = NewsArticle
    queryset = NewsArticle.objects.filter(visible=True)
    template_name = "events.html"
    ordering = "-event_date"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = "events"
        return context


class NewsArticleDetailView(DetailView):
    model = NewsArticle
    template_name = "event.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = "events"
        return context
