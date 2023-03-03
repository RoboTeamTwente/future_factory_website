from django.db import models

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
