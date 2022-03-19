# Generated by Django 4.0.3 on 2022-03-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdbox', '0010_rename_region_id_watcher_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='watcher',
        ),
        migrations.AddField(
            model_name='sighting',
            name='watcher',
            field=models.ManyToManyField(related_name='Watcher', to='birdbox.watcher'),
        ),
    ]
