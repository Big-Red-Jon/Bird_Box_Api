from django.db import models


class Location(models.Model):

    region = models.CharField(
        null=True,
        max_length=25,
        default="location not currently available"
    )

    state = models.CharField(
        null=True,
        max_length=15,
        default="State Not Available in Region"
    )

    country = models.CharField(
        null=True,
        max_length=10,
        default="No County Available in Area"
    )

    class Meta:
        app_label = "birdbox"
