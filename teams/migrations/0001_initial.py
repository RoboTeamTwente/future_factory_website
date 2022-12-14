# Generated by Django 4.1.2 on 2022-10-25 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=250)),
                ('contact_person_function', models.CharField(max_length=100)),
                ('contact_mail', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('banner_picture', models.ImageField(upload_to='teams')),
                ('logo', models.ImageField(upload_to='teams')),
                ('slogan', models.CharField(max_length=250)),
                ('team_picture', models.ImageField(upload_to='teams')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamTextSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='teams')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='teams.team')),
            ],
        ),
    ]
