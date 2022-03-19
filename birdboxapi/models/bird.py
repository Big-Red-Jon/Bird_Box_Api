from django.db import models
from .location import Location
# from .song import Song
from .taxonomy import Taxonomy


class Bird(models.Model):

    common_name = models.ForeignKey(
        Taxonomy,
        verbose_name="Common Name",
        null=True,
        on_delete=models.SET_NULL
    )
    #  location = models.ManyToManyField(
    #     Location,
    #     related_name="state",
    # )
    location = models.ForeignKey(
        Location,
        verbose_name="Region",
        null=True,
        on_delete=models.SET_NULL
    )
    # song = models.ForeignKey(
    #     Song,
    #     verbose_name="Song",
    #     null=True,
    #     on_delete=models.SET_NULL
    # )
    bird_img = models.URLField(
        null=True,
        max_length=500
    )

    class Meta:
        app_label = "birdbox"
