# Generated by Django 4.1.3 on 2023-02-24 21:44

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_teamtextsection_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_picture',
        ),
        migrations.AddField(
            model_name='team',
            name='main_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
