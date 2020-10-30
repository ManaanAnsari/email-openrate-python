from django.db import models

# Create your models here.
class ImageHash(models.Model):
    i_hash = models.TextField(unique=True)
    status = models.BooleanField(default= False) 

