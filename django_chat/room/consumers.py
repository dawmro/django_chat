import json

# class for creating consumer
from channels.generic.websocket import AsyncWebsocketConsumer
# for storing things into database inside asynchronous view
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User

from .models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    # handle connection
    async def connect(self):
        # select correct room based on url
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # setup group name
        self.room_group_name = 'chat_%s' % self.room_name

        # join channel
        await self.channel_layer.group_add(
            self.room_group_name,
            # created automagically
            self.channel_name
        )

        # wait for connection to server
        await self.accept()
    
    # handle disconnect
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            # created automagically
            self.channel_name
        )

    # handle new message
    async def receive(self, text_data):
        # create json object with text_data from frontend
        data = json.loads(text_data)
        # get message from json
        message = data['message']
        # get username from json
        username = data['username']
        # get room from json
        room = data['room']

        # save message to db
        await self.save_message(username, room, message)

        # send it to room_group_name
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                # object to send
                'type': 'chat_message',
                # message, username and room to send
                'message': message,
                'username': username,
                'room': room
            }
        )

    # new method for chat_message
    async def chat_message(self, event):
        # get message from json
        message = event['message']
        # get username from json
        username = event['username']
        # get room from json
        room = event['room']

        # convert data to json object, send it to selected room
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room
        }))

    # store data in database and wait for await to finish 
    @sync_to_async
    # save messages to db
    def save_message(self, username, room, message):
        # get user object
        user = User.objects.get(username=username)
        # get room object
        room = Room.objects.get(slug=room)

        # create new message object
        Message.objects.create(user=user, room=room, content=message)
         
