# Generated by Django 4.1.3 on 2023-02-25 14:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_teamfact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamfact',
            name='icon',
            field=models.CharField(help_text='This icon should be chosen from Themify Icons. You can find all available icons at https://themify.me/themify-icons. A preview can be seen in the column right.', max_length=50, validators=[django.core.validators.RegexValidator('ti-.+', message='Please fill out a valid Themify Icon string.')]),
        ),
    ]