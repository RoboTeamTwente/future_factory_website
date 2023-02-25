from django.views.generic import TemplateView

from events.models import Event
from news_articles.models import NewsArticle
from teams.models import Team


# Create your views here.
class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['current'] = "home"

        context['teams'] = Team.objects.order_by('name').all()

        # Show only the latest four, still visible events.
        context['events'] = Event.objects.filter(visible=True).order_by('-date')[:4].all()

        # Show only the latest three news articles that are visible.
        context['news_articles'] = NewsArticle.objects.filter(visible=True).order_by('-date')[:3].all()
        return context
