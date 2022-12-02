from django.views.generic import ListView, DetailView

from events.models import Event


# Create your views here.
class EventListView(ListView):
    model = Event
    queryset = Event.objects.filter(visible=True)
    template_name = "events.html"
    ordering = "-creation_date"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['current'] = "events"
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = "event.html"

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['current'] = "events"
        return context
