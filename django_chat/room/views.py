from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message

# Create your views here.

@login_required
def rooms(request):
    # get all rooms from database
    rooms = Room.objects.all()

    context = {
        'rooms': rooms
    }
    return render(request, 'room/rooms.html', context)


@login_required
def room(request, slug):
    # get specific room from db 
    room = Room.objects.get(slug=slug)
    # get 25 first messages for this room
    messages = Message.objects.filter(room=room)[0:25]

    context = {
        'room': room,
        'messages': messages
    }
    return render(request, 'room/room.html', context)