import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TicketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("tickets", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("tickets", self.channel_name)

    async def ticket_created(self, event):
        """Maneja el evento de creación de ticket."""
        await self.send(text_data=json.dumps(event["message"]))
    async def ticket_deleted(self, event):
        """Maneja el evento de eliminación de ticket."""
        await self.send(text_data=json.dumps(event["message"]))
    async def ticket_updated(self, event):
        """Maneja el evento de actualización de ticket."""
        await self.send(text_data=json.dumps(event["message"]))
