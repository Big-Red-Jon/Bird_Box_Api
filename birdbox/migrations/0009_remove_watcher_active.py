# Generated by Django 4.0.3 on 2022-03-16 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birdbox', '0008_remove_watcher_birds_sighted_id_sighting_watcher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watcher',
            name='active',
        ),
    ]
