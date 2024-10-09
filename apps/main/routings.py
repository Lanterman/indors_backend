from django.urls import path
from .consumers import consumers

websocket_urlpatterns = [
    path("ws/chat/<chat_id>", consumers.ChatConsumer.as_asgi()),
]
