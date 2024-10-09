import logging

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from . import mixins


class ChatConsumer(AsyncJsonWebsocketConsumer, mixins.SendMessageMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    async def connect(self):
        self.user = self.scope["user"]
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.lobby_group_name = f"lobby_{self.chat_id}"
        await self.channel_layer.group_add(self.lobby_group_name, self.channel_name)

        await self.accept()
    
    async def disconnect(self, close_code):
        if close_code is None:
            logging.info(msg="Websocket disconect.")
        elif close_code < 1002:
            logging.info(msg=f"Websocket disconect. Code - {close_code}")
        else: 
            logging.warning(msg=f"Emergency shutdown. Code - {close_code}")

        await self.channel_layer.group_discard(self.lobby_group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        if content["type"] == "send_message":
            data = await self._send_message(content["message"], self.chat_id, self.user.id)
            await self.channel_layer.group_send(self.lobby_group_name, data)
    
    async def send_message(self, event):
        """Called when a player sends a message to the chat"""

        logging.info("sent 'Send_message' message")
        await self.send_json(event)
