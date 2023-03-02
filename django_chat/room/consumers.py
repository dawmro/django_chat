import json

# class for creating consumer
from channels.generic.websocket import AsyncWebsocketConsumer
# for storing things into database inside asynchronous view
from asgiref.sync import sync_to_async


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