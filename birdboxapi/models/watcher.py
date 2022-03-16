from django.db import models
from django.contrib.auth.models import User
from .location import Location


# user, img, age, regionId, BirdSightedID, Active


class Watcher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    profile_image_url = models.URLField(
        null=True,
        max_length=500
    )
    age = models.CharField(
        max_length=5,
    )
    region_id = models.ForeignKey(
        Location,
        verbose_name="Location",
        null=True,
        on_delete=models.SET_NULL
    )
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "birdbox"
