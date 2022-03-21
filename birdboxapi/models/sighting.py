from django.db import models
from .bird import Bird
from .location import Location
from .watcher import Watcher


class Sighting(models.Model):

    bird = models.ForeignKey(
        Bird,
        verbose_name="Bird",
        null=True,
        on_delete=models.SET_NULL
    )
    location = models.ForeignKey(
        Location,
        verbose_name="Location",
        null=True,
        on_delete=models.SET_NULL
    )
    watcher = models.ForeignKey(
        Watcher,
        verbose_name="Watcher",
        null=True,
        on_delete=models.SET_NULL
    )
    sighted = models.DateTimeField()

    class Meta:
        app_label = "birdbox"
