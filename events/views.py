from django.views.generic import TemplateView


# Create your views here.
class EventsView(TemplateView):
    template_name = "events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = "events"
        return context


class FFWebsite(TemplateView):
    template_name = "ffwebsite.html"

    def get_context_data(self, **kwargs):
        context = super(FFWebsite, self).get_context_data(**kwargs)
        context['current'] = "events"
        return context
