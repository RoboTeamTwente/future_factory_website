from django.db import models
from django.db.models import Model
from django.urls import reverse


class Team(Model):
    name = models.CharField(max_length=100,)
    contact_person = models.CharField(max_length=250)
    contact_person_function = models.CharField(max_length=100)
    contact_mail = models.EmailField()
    website = models.URLField()

    banner_picture = models.ImageField(upload_to="teams")
    logo = models.ImageField(upload_to="teams")
    slogan = models.CharField(max_length=250)
    team_picture = models.ImageField(upload_to="teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team", args=[self.id])


class TeamTextSection(Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="teams", null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="sections")

    def __str__(self):
        return self.team.name + " - " + self.title
