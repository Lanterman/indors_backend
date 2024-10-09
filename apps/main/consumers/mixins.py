from . import db_queries
from .. import serializers, models

class SendMessageMixin:
    """Send message to lobby chat"""

    async def _send_message(self, message: str, chat_id: int, user_id: int) -> dict:
        message_instance = await self.preform_create_message(message, chat_id, user_id)
        serializer = serializers.MessageSerializer(message_instance).data
        return {"type": "send_message", "message": serializer}
    
    async def preform_create_message(self, message: str, chat_id: int, user_id: int) -> models.Message:
        query = await db_queries.create_message(message, chat_id, user_id)
        return query
