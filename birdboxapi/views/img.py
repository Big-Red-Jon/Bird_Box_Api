from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

from birdboxapi.models import img

# Incomplete Feature for Later


class UploadViewSet(ViewSet):

    def create(self, request):
        file = request.data.get('newFile')
        other_way_to_get_file = request.FILES.get('newFile')
        description = request.data.get('description')
        # s3_url = s3client.upload(file)
        upload = img(file_url=file, description=description)
        upload.save()
        return Response(UploadSerializer(upload).data, status=201)

    def list(self, request):
        return Response(
            UploadSerializer(img.objects.all(),
                             many=True).data
        )


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = img
        fields = ('id', 'description', 'file_url')
