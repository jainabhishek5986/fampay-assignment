# Generated by Django 3.2.13 on 2022-07-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('is_limit_over', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'APIKey',
                'verbose_name_plural': 'APIKeys',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField()),
                ('thumbnail_url', models.URLField(max_length=255)),
                ('video_url', models.URLField(max_length=255)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'ordering': ['-published_at'],
            },
        ),
    ]
