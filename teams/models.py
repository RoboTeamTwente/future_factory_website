from django.db import models
from django.db.models import Model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_quill.fields import QuillField

from future_factory_website.utils import compress


class Team(Model):
    name = models.CharField(max_length=100,)
    contact_person = models.CharField(max_length=250)
    contact_person_function = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=15, null=True)
    contact_mail = models.EmailField()
    website = models.URLField()

    banner_picture = models.ImageField(upload_to="teams")
    logo = models.ImageField(upload_to="teams")
    slogan = models.CharField(max_length=250)
    team_picture = models.ImageField(upload_to="teams")

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # Slugify the team name
        self.slug = slugify(self.name)

        # Compress the images that are uploaded
        self.banner_picture = compress(self.banner_picture)
        self.logo = compress(self.logo)
        self.team_picture = compress(self.team_picture)

        return super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team", args=[self.slug])


class TeamTextSection(Model):
    title = models.CharField(max_length=100)
    text = QuillField()
    image = models.ImageField(upload_to="teams", null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="sections")

    @property
    def text_html(self):
        return self.text.html.replace("<p><br></p>", "<br>").replace("<p>", "").replace("</p>", "<br>")

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress(self.image)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.team.name + " - " + self.title
