from channels.generic.websocket import AsyncJsonWebsocketConsumer

from keyua1_1.settings.common import CITIES_UPDATING_GROUP


class DashboardConsumer(AsyncJsonWebsocketConsumer):
    group_name: str = CITIES_UPDATING_GROUP
    user_id: int = None

    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.group_name = f'{CITIES_UPDATING_GROUP}_{self.user_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name)

        await self.accept()

    async def receive_json(self, content, **kwargs):
        pass

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def update_city(self, event):
        await self.send_json(event)

    async def send_data(self, event):
        await self.send_json(event)
