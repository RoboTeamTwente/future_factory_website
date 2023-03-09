from django.shortcuts import render
from django.views.generic import DetailView, ListView

from events.models import Event


class EventListView(ListView):
    model = Event
    queryset = Event.objects.filter(visible=True)
    template_name = "events.html"
    ordering = "-date"
    paginate_by = 8


class EventDetailView(DetailView):
    model = Event
    template_name = "event.html"
