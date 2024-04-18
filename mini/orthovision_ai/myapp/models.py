from django.db import models

# Create your models here.
class XrayImages(models.Model):
    img = models.ImageField(upload_to='Xrayimages/')