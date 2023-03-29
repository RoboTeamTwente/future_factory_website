from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_quill.fields import QuillField

from facts.models import Fact
from future_factory_website.utils import compress


class Team(Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=250)
    contact_person_function = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=15, null=True)
    contact_mail = models.EmailField()
    website = models.URLField()

    front_page_picture = models.ImageField(upload_to="teams", help_text="This image is used to create the hexagon on the main page. THIS PICTURE HAS TO BE SQUARE.")
    banner_picture = models.ImageField(upload_to="teams",
                                       help_text="This picture will serve as the background on your team's page.")
    logo = models.ImageField(upload_to="teams", validators=[FileExtensionValidator(['png'])],
                             help_text="This should be in a PNG format")
    logo_svg = models.FileField(upload_to="teams", validators=[FileExtensionValidator(['svg'])],
                                help_text="This should be in a SVG format", blank=True, null=True)
    main_color = ColorField(help_text="In most cases this would be your teams color. It is used to color the headers and icons on your team's page.")
    slogan = models.CharField(max_length=250)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # Slugify the team name
        self.slug = slugify(self.name)

        # Compress the images that are uploaded
        if self.front_page_picture:
            self.front_page_picture = compress(self.front_page_picture)

        if self.banner_picture:
            self.banner_picture = compress(self.banner_picture)

        return super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team", args=[self.slug])


class TeamAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team_account')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class TeamTextSection(Model):
    title = models.CharField(max_length=100, null=True, blank=True)
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
        return self.team.name + " - " + (self.title if self.title else 'section')


class TeamFact(Fact):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="facts")