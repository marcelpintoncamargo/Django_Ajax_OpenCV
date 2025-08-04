from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

ACTION_CHOICES = (
    ('NO_FILTER' , 'no filter'),
    ('HSV'       , 'hsv'),
    ('GRAYSCALE' , 'grayscale'),
    ('BLURRED'   , 'blurred'),
    ('BINARY'    , 'binary'),
    ('INVERT'    , 'invert'),
)

class Upload(models.Model):
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'opencv_images')
    action = models.CharField(max_length=50, choices = ACTION_CHOICES)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.image)

    def save(self, *args, **kwargs):
        # open image
        pil_img = Image.open(self.image)

        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)  ## Function imported from utils.py (ImageAnalysis)

        # convert back to pil image
        img_pil = Image.fromarray(img)

        #save
        buffer = BytesIO()
        img_pil.save(buffer, format = 'png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save = False)

        super().save(*args, **kwargs)


