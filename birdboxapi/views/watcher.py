from django.core.exceptions import ValidationError
from django.views import View
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from birdboxapi.models import Watcher, Location
from django.contrib.auth.models import User


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
        serializer = WatcherSerializer(
            watcher, many=True, context={'request': request})
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
    region_id = LocationSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Watcher
        fields = ('id', 'user', 'profile_image_url',
                  'age', 'region_id', 'created_on')
