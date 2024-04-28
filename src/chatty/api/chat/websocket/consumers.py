import json
from api.user.models import User as UserModel
from api.chat.models import Session as ChatRoomSessionModel, Message as MessageModel
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatWSConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.session_id = self.scope['url_route']['kwargs']['session_id']
        self.user = self.scope['user']

        print(type(self.session_id))
        print(self.user.id)
        

        # print(ChatRoomSessionModel.objects.filter(members__id=1))

        
        self.user_room_sessions = await database_sync_to_async(list)(ChatRoomSessionModel.objects.filter(members=str(self.user.id)).filter(id=str(self.session_id)))
        
        # check if authenticated user is a member of the session
        if not self.user_room_sessions:
            await self.close()
            
        
        
        await self.accept()
        

    def disconnect(self, code):
        ...

    def receive(self, txt):
        j = json.loads(txt)


