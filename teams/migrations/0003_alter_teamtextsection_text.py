# Generated by Django 4.1.3 on 2022-12-02 20:02

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_contact_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamtextsection',
            name='text',
            field=django_quill.fields.QuillField(),
        ),
    ]
