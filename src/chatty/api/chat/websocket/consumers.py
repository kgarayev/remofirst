import json

from api.chat.models import Session as ChatRoomSessionModel
from api.chat.websocket.serializer import WSMessageSerializer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from django.core.exceptions import ValidationError


class ChatWSConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.session_id = self.scope["url_route"]["kwargs"]["session_id"]

        self.user = self.scope["user"]

        print(type(self.session_id))
        print(self.user)

        if not self.user.is_authenticated:
            await self.close(403)

        # print(ChatRoomSessionModel.objects.filter(members__id=1))
        self.user_room_sessions = None
        try:
            print(str(self.user.id), str(self.session_id))
            self.user_room_sessions = await database_sync_to_async(list)(
                ChatRoomSessionModel.objects.filter(members=str(self.user.id)).filter(id=str(self.session_id))
            )
        except ValidationError as e:
            print(e)
            await self.close(403)

        except Exception as e:
            print(e)
            await self.close()

        # check if authenticated user is a member of the session
        if not self.user_room_sessions:
            # await self.disconnect(403)
            await self.close(403)

        self.channel_layer = get_channel_layer()

        await self.channel_layer.group_add(self.session_id, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.session_id, self.channel_name)

    async def receive(self, text_data):

        recieved_data = json.loads(text_data)

        print(type(recieved_data))

        serialized = WSMessageSerializer(data=recieved_data)

        # print(serialized.initial_data)
        # print(self.scope)
        d = None
        if serialized.is_valid():

            d = serialized.data

        if d:
            await self.channel_layer.group_send(
                self.session_id,
                {"type": "message_handler", "room_id": self.session_id, "username": self.user.username, "message": d["message_body"]},
            )
        # await self.channel_layer.group_send(
        #     self.session_id,
        #     {
        #         "type": "chat.message",
        #         "message": serialized.data
        #     }
        # )

    async def message_handler(self, event):
        message = event["message"]
        await self.send(text_data=message)
