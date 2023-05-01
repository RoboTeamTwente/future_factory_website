from django.db import models
from django.db.models import Model
from django.urls import reverse
from django_quill.fields import QuillField

from future_factory_website.utils import compress


class NewsArticle(Model):
    title = models.CharField(max_length=100, help_text="This will be the title of the news article")
    summary = models.CharField(max_length=250, help_text="Shown as a side text on the frontpage and news page")
    image = models.ImageField(upload_to='news_articles', null=True, blank=True)
    visible = models.BooleanField(default=True)
    date = models.DateField()

    class Meta:
        verbose_name = "news article"
        verbose_name_plural = "news articles"

    @property
    def description_html(self):
        return self.description.html.replace("<p><br></p>", "<br>").replace("<p>", "").replace("</p>", "<br>")

    def get_absolute_url(self):
        return reverse("news_article", args=[self.id])

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    text = QuillField(blank=True, null=True)
    image = models.ImageField(upload_to='news_articles', blank=True, null=True)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name='paragraphs')

    @property
    def text_html(self):
        return self.text.html.replace("<p><br></p>", "<br>").replace("<p>", "").replace("</p>", "<br>")

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress(self.image)
        super().save(*args, **kwargs)