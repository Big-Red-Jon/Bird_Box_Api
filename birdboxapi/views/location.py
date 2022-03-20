from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from birdboxapi.models import Location
from rest_framework.decorators import api_view


# @api_view(['GET'])
# def get_location_array(request):
#     watcher = request.auth.user.watcher
#     serializer = LocationSerializer(watcher)

#     return Response(serializer.data)


class LocationView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            location = Location.objects.get(pk=pk)
            serializer = LocationSerializer(
                location, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(
            locations, many=True, context={'request': request})
        return Response(serializer.data)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'region', 'state', 'country')
