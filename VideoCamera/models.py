from django.db import models
from django.utils import timezone


class ImageCamera_Model(models.Model):
    id = models.AutoField(primary_key = True)
    # name = models.CharField(max_length= 100)
    # description = models.TextField()
    image = models.FileField(upload_to = 'camera_images')
    created_at = models.DateTimeField(default = timezone.now)
    #created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.id)