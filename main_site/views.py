from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from events.models import Event
from future_factory_website.forms import ContactForm
from main_site.models import Email, PressPicture
from news_articles.models import NewsArticle
from teams.models import Team


# Create your views here.
class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        context['teams'] = Team.objects.order_by('name').all()

        # Show only the latest four, still visible events.
        context['events'] = Event.objects.filter(visible=True).order_by('-date')[:4].all()

        # Show only the latest three news articles that are visible.
        context['news_articles'] = NewsArticle.objects.filter(visible=True).order_by('-date')[:3].all()

        # Add in our contact form
        context['contact_form'] = ContactForm()
        return context


class PressView(TemplateView):
    template_name = "press.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.order_by('name').all()
        context['pictures'] = PressPicture.objects.all()
        return context


class SendMessage(View):
    team = None

    def post(self, request, slug=None):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            Email.objects.create(email_sender=contact_form.cleaned_data['sender_mail'],
                                 recipient=self.team,
                                 message=contact_form.cleaned_data['message'])
            messages.success(request, message="Your email was successfully send")
        else:
            for field in contact_form.errors:
                messages.error(request, message=contact_form.errors.get_json_data()[field][0]['message'])

        if self.team:
            return redirect(reverse("team", args=[self.team.slug]) + "#contact")
        else:
            return redirect(reverse("home") + "#contact")
