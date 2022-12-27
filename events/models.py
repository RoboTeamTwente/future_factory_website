from django.db import models
from django.db.models import Model
from django.urls import reverse
from django_quill.fields import QuillField

from future_factory_website.utils import compress


# Create your models here.
class Event(Model):
    title = models.CharField(max_length=100, help_text="This will be the title of the news article")
    summary = models.CharField(max_length=250, help_text="Shown as a side text on the frontpage and news page")
    description = QuillField()
    image = models.ImageField(upload_to='events', null=True, blank=True)
    visible = models.BooleanField(default=True)
    event_date = models.DateField()

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    @property
    def description_html(self):
        return self.description.html.replace("<p><br></p>", "<br>").replace("<p>", "").replace("</p>", "<br>")

    def get_absolute_url(self):
        return reverse("event", args=[self.id])

    def save(self, *args, **kwargs):
        if self.image:
            new_image = compress(self.image)
            self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
