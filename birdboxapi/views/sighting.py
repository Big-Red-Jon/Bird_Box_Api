from django import views
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from birdboxapi.models import Sighting, Bird, Watcher, Location, Taxonomy
from django.contrib.auth.models import User


class SightingView(ViewSet):

    def create(self, request):

        watcher = Watcher.objects.get(user=request.auth.user)

        location = Location.objects.get(pk=request.data["location"])
        bird = Bird.objects.get(pk=request.data["bird"])

        sighting = Sighting()
        sighting.bird = bird
        sighting.location = location
        sighting.sighted = request.data["sighted"]
        sighting.watcher = watcher

        try:
            sighting.save()
            serializer = SightingSerializer(
                sighting, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            sighting = Sighting.objects.get(pk=pk)
            serializer = SightingSerializer(
                sighting, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        sighting = Sighting.objects.get(pk=pk)
        sighting.sighted = request.data["sighted"]

        watcher = Watcher.objects.get(user=request.auth.user)
        sighting.watcher = watcher

        location = Location.objects.get(pk=request.data["location"])
        sighting.location = location
        bird = Bird.objects.get(pk=request.data["bird"])
        sighting.bird = bird
        sighting.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            sighting = Sighting.objects.get(pk=pk)
            sighting.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Sighting.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        sightings = Sighting.objects.all()

        location = self.request.query_params.get('type', None)
        if location is not None:
            sightings = sightings.filter(location_id=location)

        bird = self.request.query_params.get('type', None)
        if bird is not None:
            sightings = sightings.filter(bird_id=bird)

        watcher = self.request.query_params.get('type', None)
        if watcher is not None:
            watcher = sightings.filter(watcher_id=watcher)

        serializer = SightingSerializer(
            sightings, many=True, context={'request': request})
        return Response(serializer.data)


class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ('id', 'Kingdom', 'Phylum', 'Class', 'Order',
                  'Family', 'Genus', 'Species', 'CommonName')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'region', 'state', 'country')


class BirdSerializer(serializers.ModelSerializer):
    common_name = TaxonomySerializer(many=False)
    location = LocationSerializer(many=True)

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
