# Generated by Django 4.1.3 on 2023-05-01 15:00

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


def move_paragraphs(apps, schema_editor):
    NewsArticle = apps.get_model('news_articles', 'NewsArticle')
    Paragraph = apps.get_model('news_articles', 'Paragraph')
    for news_article in NewsArticle.objects.all():
        Paragraph.objects.create(text=news_article.description, article=news_article)


def undo_move_paragraph(apps, schema_editor):
    Paragraph = apps.get_model('news_article', 'Paragraph')
    for paragraph in Paragraph.objects.all():
        news_article = paragraph.article.description = paragraph.text
        news_article.save()
        paragraph.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0008_alter_newsarticle_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', django_quill.fields.QuillField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_articles')),
                ('article',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_articles.newsarticle')),
            ],
        ),
        migrations.RunPython(move_paragraphs, undo_move_paragraph),
        migrations.RemoveField(
            model_name='newsarticle',
            name='description',
        ),
    ]
