from django.db import models
from django.utils.safestring import mark_safe

from future_factory_website.utils import compress
from teams.models import Team


class PressPicture(models.Model):
    picture = models.ImageField(upload_to="press")
    thumbnail = models.ImageField(upload_to="press", blank=True)

    class Meta:
        verbose_name = "press picture"
        verbose_name_plural = "press pictures"

    def image_preview(self):
        if self.thumbnail:
            return mark_safe(f"<img src='{self.thumbnail.url}' style='width:200px'>")

    def save(self, *args, **kwargs):
        if self.picture:
            self.thumbnail = compress(image=self.picture, quality=40)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.picture.name
