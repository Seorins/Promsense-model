import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(">>>> receive called")  # 디버깅용
        data = json.loads(text_data)
        username = data['username']
        message = data['message']
        liked = data.get('liked', False)

        # 저장
        saved_message = await self.save_message(username, message, liked)

        # 클라이언트로 전송
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'id': saved_message.id,
                'username': username,
                'message': message,
                'timestamp': saved_message.timestamp.strftime("%Y-%m-%d %H:%M"),
                'liked': liked,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'id': event['id'],
            'username': event['username'],
            'message': event['message'],
            'timestamp': event['timestamp'],
            'liked': event['liked'],
        }))

    @sync_to_async
    def save_message(self, username, message, liked):

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None  # 로그인 안 한 경우

        if user is not None:
            msg = Message.objects.create(user=user, message=message, liked=liked)
            return msg
        else:
            return None