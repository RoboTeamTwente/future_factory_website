# Generated by Django 4.1.3 on 2022-12-02 19:12

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
    ]