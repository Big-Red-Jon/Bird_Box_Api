from django.db import models


class Taxonomy(models.Model):

    Kingdom = models.CharField(
        max_length=50,
        default='Unknown'
    )

    Phylum = models.CharField(
        max_length=50,
        default='Unknown'
    )

    Class = models.CharField(
        max_length=50,
        default='Unknown'
    )

    Order = models.CharField(
        max_length=50,
        default='Unknown'
    )

    Family = models.CharField(
        max_length=50,
        default='Unknown'
    )

    Genus = models.CharField(
        max_length=50,
        default='Unknown'
    )

    Species = models.CharField(
        max_length=50,
        default='Unknown'
    )

    CommonName = models.CharField(
        max_length=50,
        default='Unknown'
    )

    class Meta:
        app_label = "birdbox"
