from django.views.generic import TemplateView

from news_articles.models import NewsArticle


# Create your views here.
class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['current'] = "home"

        # Show only the latest four, still visible events.
        context['events'] = []

        context['news_articles'] = NewsArticle.objects.filter(visible=True).order_by('-date')[:3].all()
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['current'] = "contact"
        return context
