import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from asgiref.sync import sync_to_async
from .models import SpeedData

class Speedometer(AsyncWebsocketConsumer):
    async def connect(self):
        
        await self.channel_layer.group_add("speedometer_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard("speedometer_group", self.channel_name)

    @sync_to_async
    def save_speed_data(self, speed):
        
        return SpeedData.objects.create(speed=speed)

    async def receive(self, text_data):
        
        data = json.loads(text_data)
        speed = data.get('speed', 0)

        
        speed_instance = await self.save_speed_data(speed)

        
        await self.channel_layer.group_send(
            "speedometer_group",
            {
                "type": "speed_update",
                "speed": speed,
                "timestamp": str(speed_instance.timestamp)
            }
        )

    async def speed_update(self, event):
      
        await self.send(text_data=json.dumps({
            'speed': event['speed'],
            'timestamp': event['timestamp']
        }))