from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView

from future_factory_website.forms import ContactForm
from main_site.models import Email
from main_site.views import SendMessage
from teams.models import Team


class TeamDetailView(DetailView):
    model = Team
    template_name = "team.html"

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        context['text_sections'] = self.object.sections.order_by('id').all()
        return context


class TeamEmailView(SendMessage):

    def post(self, request, slug=None):
        try:
            self.team = Team.objects.get(slug=slug)
        except Team.DoesNotExist:
            raise Http404()

        return super().post(request, slug)
