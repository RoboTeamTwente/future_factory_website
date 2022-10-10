from django.views.generic import TemplateView


# Create your views here.
class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['current'] = "home"
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['current'] = "contact"
        return context


class OOFFView(TemplateView):
    template_name = "ooff.html"
