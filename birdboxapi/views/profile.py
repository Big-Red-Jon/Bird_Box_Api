from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from birdboxapi.models import Watcher, Sighting, Location, Bird, Taxonomy
from birdboxapi.views.watcher import WatcherSerializer


class Profile(ViewSet):

    def list(self, request):

        watcher = Watcher.objects.get(user=request.auth.user)
        sightings = Sighting.objects.filter(watcher=watcher)

        watcher = WatcherSerializer(
            watcher, many=False, context={'request': request})

        sightings = SightingSerializer(
            sightings, many=False, context={'request': request})

        profile = {}
        profile["watcher"] = watcher.data
        profile["sightings"] = sightings.data

        return Response(profile)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'region', 'state', 'country')


class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ('id', 'Kingdom', 'Phylum', 'Class', 'Order',
                  'Family', 'Genus', 'Species', 'CommonName')


class BirdSerializer(serializers.ModelSerializer):
    common_name = TaxonomySerializer(many=False)
    location = LocationSerializer(many=False)

    class Meta:
        model = Bird
        fields = ("id", "common_name", "location", "bird_img")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class WatcherSerializer(serializers.ModelSerializer):
    region = LocationSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Watcher
        fields = ('id', 'user', 'profile_image_url',
                  'age', 'region', 'created_on')


class SightingSerializer(serializers.ModelSerializer):
    bird = BirdSerializer(many=False)
    location = LocationSerializer(many=False)
    watcher = WatcherSerializer(many=False)

    class Meta:
        model = Sighting
        fields = ("id", "bird", "location", "watcher", "sighted")
