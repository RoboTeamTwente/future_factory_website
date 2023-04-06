# Generated by Django 4.1.3 on 2023-04-06 11:36

from django.db import migrations, models
from django.db.models import F


def copy_start_time(apps, schema_editor):
    Event = apps.get_model('events', 'Event')
    Event.objects.all().update(end=F('start'))


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_visible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='start',
        ),
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(help_text='When does this event end?', null=True),
        ),
        migrations.RunPython(
            copy_start_time,
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(help_text='When does this event end?'),
        )
    ]
