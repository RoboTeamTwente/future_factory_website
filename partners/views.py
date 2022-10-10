from django.views.generic import TemplateView


# Create your views here.
class PartnerView(TemplateView):
    template_name = "partners.html"

    def get_context_data(self, **kwargs):
        context = super(PartnerView, self).get_context_data(**kwargs)
        context['current'] = "partners"
        return context
