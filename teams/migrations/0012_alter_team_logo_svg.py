# Generated by Django 4.1.3 on 2023-03-04 14:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_team_logo_svg_alter_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo_svg',
            field=models.FileField(blank=True, help_text='This should be in a SVG format', null=True, upload_to='teams', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]
