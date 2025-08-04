from django.db import models


class PhotoModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'ajax_images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    

