import datetime

from django.db import models
from django.urls import reverse

from config import settings
from .services import HairinessChoice


User = settings.AUTH_USER_MODEL


class Cat(models.Model):
    """The cat model"""

    name: str = models.CharField("name", max_length=250, help_text="Required.")
    age: str = models.IntegerField("age")
    breed: str = models.CharField("breed", max_length=250, help_text="Required.")
    hairiness: str = models.CharField("haireness", max_length=30, default=HairinessChoice.MEDIUM, help_text="Required.", 
                                         choices=HairinessChoice.choices)
    created_in: datetime.datetime = models.DateTimeField(auto_now_add=True)
    owner_id = models.ForeignKey(to=User, verbose_name="user", on_delete=models.CASCADE, related_name="cats")

    class Meta:
        verbose_name = "Cat"
        verbose_name_plural = "Cats"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat-detail', kwargs={'id': self.id})


class Chat(models.Model):
    "The Chat model"

    created_in: datetime.datetime = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(to=User, verbose_name="users", related_name="chats")

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('chat-detail', kwargs={'id': self.id})


class Message(models.Model):
    "The Message model"

    message: str = models.TextField("message")
    created_in: datetime.datetime = models.DateTimeField(auto_now_add=True)
    chat_id: int = models.ForeignKey(to=Chat, verbose_name="chat", on_delete=models.CASCADE, related_name="messages")
    owner_id: int = models.ForeignKey(to=User, verbose_name="owner", on_delete=models.CASCADE, related_name="user_messages")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('message-detail', kwargs={'id': self.id})
