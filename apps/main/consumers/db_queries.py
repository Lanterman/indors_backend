from .. import models


async def create_message(message: str, chat_id: int, owner_id: int) -> models.Message:
    """Create message model instance and return it"""

    query = await models.Message.objects.acreate(message=message, chat_id=chat_id, owner_id=owner_id)
    return query
