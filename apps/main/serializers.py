from rest_framework import serializers

from . import models
from apps.user.serializers import MyProfileSerializer

class CreateCatSerializer(serializers.ModelSerializer):
    """Create a cat serializer"""

    class Meta:
        model = models.Cat
        fields = ["name", "age", "breed", "hairiness"]


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


class ChatSerializer(serializers.ModelSerializer):
    """A chat serializer"""

    users = MyProfileSerializer(many=True)
    
    class Meta:
        model = models.Chat
        fields = ("id", "users")