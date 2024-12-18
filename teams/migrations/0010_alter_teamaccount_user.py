# Generated by Django 4.1.3 on 2023-03-03 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0009_teamaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamaccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_account', to=settings.AUTH_USER_MODEL),
        ),
    ]
