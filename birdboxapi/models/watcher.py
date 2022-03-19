from django.db import models
from django.contrib.auth.models import User
from .location import Location


class Watcher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    # sighting_watcher = models.ManyToManyField(
    #     Sighting, related_name=("sighting"))

    profile_image_url = models.URLField(
        null=True,
        max_length=500
    )
    age = models.CharField(
        max_length=5,
    )
    region = models.ForeignKey(
        Location,
        verbose_name="Location",
        null=True,
        on_delete=models.SET_NULL
    )
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "birdbox"
