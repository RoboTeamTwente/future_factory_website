from django.db import models
from django.db.models import Model
from django.urls import reverse


# Create your models here.
class Event(Model):
    summary = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    description = models.TextField(help_text="Warning! This field allows for the use of HTML tags. Be cautious since there are no checks in place. ALWAYS check the page immediately after creation.")
    image = models.ImageField(upload_to='events', null=True, blank=True)
    visible = models.BooleanField(default=True)
    creation_date = models.DateField()

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def get_absolute_url(self):
        return reverse("event", args=[self.id])

    def __str__(self):
        return self.summary
