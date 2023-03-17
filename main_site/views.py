import datetime
from smtplib import SMTPException

from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, mail_admins
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from events.models import Event
from future_factory_website.forms import ContactForm
from main_site.models import PressPicture
from news_articles.models import NewsArticle
from teams.models import Team


# Create your views here.
class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        context['teams'] = Team.objects.order_by('name').all()

        # Show only the latest four, still visible events.
        context['events'] = Event.objects.filter(visible=True, date__gte=datetime.datetime.now()).order_by('-date')[:4].all()

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
            message = f"You got a new message from the Future Factory website!\n\nFrom: {contact_form.cleaned_data['sender_mail']}\n\nMessage: {contact_form.cleaned_data['message']}"
            try:
                send_mail(subject="[Future Factory Website] General contact form",
                          from_email='noreply@roboteamtwente.nl',
                          recipient_list=[self.team.contact_mail if self.team else 'info@futurefactorytwente.nl'],
                          message=message)
                messages.success(request, message="Your email was successfully send")
            except SMTPException as e:
                messages.error(request, message="The server cannot send your email. Please try again later.")
                mail_admins(subject="[Contact Form] Failed sending email", message=str(e))
            except BadHeaderError:
                messages.error(request, message="Your email seems to be malformed, please try again.")
        else:
            for field in contact_form.errors:
                messages.error(request, message=contact_form.errors.get_json_data()[field][0]['message'])

        if self.team:
            return redirect(reverse("team", args=[self.team.slug]) + "#contact")
        else:
            return redirect(reverse("home") + "#contact")
