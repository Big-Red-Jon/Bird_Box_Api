from django.core.exceptions import ValidationError
from django.views import View
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from birdboxapi.models import Watcher, Location, Sighting
from django.contrib.auth.models import User
from .sighting import SightingSerializer


class WatcherView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            watcher = Watcher.objects.get(pk=pk)
            serializer = WatcherSerializer(
                watcher, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        watcher = Watcher.objects.all()
        watcher = WatcherSerializer(
            watcher, many=True, context={'request': request})

        profile = {}
        profile["watcher"] = watcher.data
        return Response(profile)

    @action(methods=["GET"], detail=True)
    def sightings(self, request, pk=None):
        watcher_sightings = Sighting.objects.filter(watcher=pk)
        serializer = SightingSerializer(watcher_sightings, context={
                                        'request: request'}, many=True)
        return Response(serializer.data)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'region', 'state', 'country')


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
