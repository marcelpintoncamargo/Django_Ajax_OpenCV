from django.db import models

class SaveImageModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pacoca_air')
    created = models.DateTimeField(auto_now_add=True)