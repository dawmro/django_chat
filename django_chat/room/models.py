from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Room(models.Model):
    # long name of the room
    name = models.CharField(max_length=255)
    # short name of the room used in url
    slug = models.SlugField(unique=True)


# database model for messages
class Message(models.Model):
    # get correct room
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    # get user that created message
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    # content of message
    content = models.TextField()
    # when message was created, set automagically when saved to database
    date_added = models.DateTimeField(auto_now_add=True)

    # tweak some settings
    class Meta:
        ordering = ('date_added',)
