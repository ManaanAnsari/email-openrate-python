from django.db import models

# Create your models here.
class ImageHash(models.Model):
    # store unique hash
    i_hash = models.TextField(unique=True)
    # flag to see if email opened
    status = models.BooleanField(default= False) 

