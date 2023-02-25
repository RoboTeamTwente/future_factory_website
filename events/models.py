from django.db import models
from django.urls import reverse
from django_quill.fields import QuillField

from future_factory_website.utils import compress


class Event(models.Model):
    title = models.CharField(max_length=100, help_text='This will be the title of this event')
    summary = models.CharField(max_length=250, help_text='This will be the text that is displayed on the front page, together with the event')
    description = QuillField()
    image = models.ImageField(upload_to='events', null=True, blank=True)
    visible = models.BooleanField(default=True)
    date = models.DateTimeField(help_text='When does this event take place?')
    location = models.CharField(max_length=100, help_text='Where does this event take place?')

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
            self.image = compress(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title