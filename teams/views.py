from django.views.generic import TemplateView, DetailView
from django.views.generic.base import ContextMixin

from teams.models import Team


class TeamDetailView(DetailView):
    model = Team
    template_name = "team.html"

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['current'] = "teams"
        return context

class TeamMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(TeamMixin, self).get_context_data(**kwargs)
        context['current'] = "teams"
        return context


class DroneTeamView(TemplateView, TeamMixin):
    template_name = "drone_team.html"


class ElectricSuperBikeView(TemplateView, TeamMixin):
    template_name = "electric_superbike.html"


class GreenTeamView(TemplateView, TeamMixin):
    template_name = "green_team.html"


class RoboTeamView(TemplateView, TeamMixin):
    template_name = "robo_team.html"


class SolarBoatView(TemplateView, TeamMixin):
    template_name = "solar_boat.html"
