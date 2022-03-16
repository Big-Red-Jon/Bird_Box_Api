from django.db import models


class ImgUpload(models.Model):
    file_url = models.FileField(upload_to='photos/%Y/%m/%d/')
    description = models.CharField(max_length=240)
