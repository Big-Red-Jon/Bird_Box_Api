# Generated by Django 4.0.3 on 2022-03-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdbox', '0015_alter_sighting_sighted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='sighted',
            field=models.DateField(auto_now_add=True),
        ),
    ]