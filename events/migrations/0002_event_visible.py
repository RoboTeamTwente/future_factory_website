# Generated by Django 4.1.3 on 2023-02-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]