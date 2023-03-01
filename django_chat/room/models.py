from django.db import models

# Create your models here.


class Room(models.Model):
    # long name of the room
    name = models.CharField(max_length=255)
    # short name of the room used in url
    slug = model.SlugField(unique=True)
