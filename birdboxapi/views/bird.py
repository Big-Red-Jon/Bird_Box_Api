from django.core.exceptions import ValidationError
from django.views import View
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from birdboxapi.models import Bird
from birdboxapi.models.location import Location
from birdboxapi.models.taxonomy import Taxonomy


class BirdView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            bird = Bird.objects.get(pk=pk)
            serializer = BirdSerializer(bird, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        birds = Bird.objects.all()

        location = self.request.query_params.get('type', None)
        if location is not None:
            birds = birds.filter(location_id=location)

        song = self.request.query_params.get('type', None)
        if song is not None:
            birds = birds.filter(song_id=song)

        serializer = BirdSerializer(
            birds, many=True, context={'request': request})
        return Response(serializer.data)


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
        fields = ('id', 'common_name', 'location', 'bird_img')
