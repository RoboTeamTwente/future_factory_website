from django.db import models
from django.db.models import Model
from django.urls import reverse
from django_quill.fields import QuillField


# Create your models here.
class Event(Model):
    summary = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    description = QuillField()
    image = models.ImageField(upload_to='events', null=True, blank=True)
    visible = models.BooleanField(default=True)
    creation_date = models.DateField()

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    @property
    def description_html(self):
        return self.description.html.replace("<p><br></p>", "<br>").replace("<p>", "").replace("</p>", "<br>")

    def get_absolute_url(self):
        return reverse("event", args=[self.id])

    def __str__(self):
        return self.summary
