from django.db import models
from django.utils.safestring import mark_safe

from future_factory_website.utils import compress
from teams.models import Team


class Email(models.Model):
    email_sender = models.EmailField(verbose_name="From", help_text="The email from the person that sent this mail.")
    recipient = models.ForeignKey(Team, verbose_name="To", help_text="For which team is this email meant?",
                                  on_delete=models.CASCADE, related_name="emails", null=True, blank=True)
    message = models.CharField(max_length=500, help_text="The original message as send by the messenger.")
    read = models.BooleanField(default=False, help_text="Whether this email is already read by someone.")

    def receiver(self):
        return self.recipient if self.recipient else 'Future Factory'

    def __str__(self):
        return f"{self.email_sender} -> {self.recipient if self.recipient else 'Future Factory'}"


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
