from django.views.generic import DetailView

from teams.models import Team


class TeamDetailView(DetailView):
    model = Team
    template_name = "team.html"

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['current'] = "teams"
        return context
