from rest_framework import serializers

from . import models


class CreateCatSerializer(serializers.ModelSerializer):
    """Create a cat serializer"""

    class Meta:
        model = models.Cat
        fields = ["id", "name", "age", "breed", "hairiness"]
        extra_kwargs = {"id": {"read_only": True}}


class CatSerializer(serializers.ModelSerializer):
    """A cat serializer"""

    class Meta:
        model = models.Cat
        fields = ("id", "name", "age", "breed", "hairiness", "created_in")


class UpdateCatSerializer(serializers.ModelSerializer):
    """Update a cat serializer"""

    class Meta:
        model = models.Cat
        fields = ["name", "age", "breed", "hairiness"]


class MessageSerializer(serializers.ModelSerializer):
    """A message serializer"""

    class Meta:
        model = models.Message
        fields = ("id", "message", "chat_id", "owner_id", "created_in")


class ChatSerializer(serializers.ModelSerializer):
    """A chat serializer"""

    messages = MessageSerializer(many=True)
    
    class Meta:
        model = models.Chat
        fields = ("id", "users", "messages")
