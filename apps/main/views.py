from django.utils.decorators import method_decorator
from django.db.models import Count
from django.http.response import HttpResponseRedirect
from rest_framework import generics, decorators
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from . import models, serializers, permissions


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["cats"]))
@method_decorator(name="post", decorator=swagger_auto_schema(tags=["cats"]))
class ListCatView(generics.ListCreateAPIView):
    """List user cats and create a cat endpoints"""

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Cat.objects.filter(owner_id_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CreateCatSerializer
        elif self.request.method == "GET":
            return serializers.CatSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["cat"]))
@method_decorator(name="put", decorator=swagger_auto_schema(tags=["cat"]))
@method_decorator(name="patch", decorator=swagger_auto_schema(tags=["cat"]))
@method_decorator(name="delete", decorator=swagger_auto_schema(tags=["cat"]))
class CatView(generics.RetrieveUpdateDestroyAPIView):
    """Cat endpoint"""

    queryset = models.Cat.objects.all()
    permission_classes = [IsAuthenticated, permissions.IsOwner]
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH", "POST"):
            return serializers.UpdateCatSerializer
        elif self.request.method == "GET":
            return serializers.CatSerializer
 

@method_decorator(name="get", decorator=swagger_auto_schema(tags=["chats"]))
class ListChatView(generics.ListAPIView):
    """Show chat list or create a chat - endpoints"""

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        return models.Chat.objects.filter(users__in=[self.request.user.id]).prefetch_related("users")


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["chats"]))
class ChatView(generics.RetrieveAPIView):
    """Chat endpoint"""

    queryset = models.Chat.objects.all().prefetch_related("messages")
    serializer_class = serializers.ChatSerializer
    permission_classes = [IsAuthenticated, permissions.IsExistsInChat]
    lookup_field = "id"


@decorators.api_view(["GET"])
@decorators.permission_classes([IsAuthenticated])
def create_chat_view(request, user_id: int) -> None:
    """Create chat if it doesn't exist"""

    chats = models.Chat.objects.filter(users__in=[request.user.id, user_id]).annotate(c=Count('users')).filter(c=2)
    if chats.count():
        chat = chats.first()
    else:
        chat = models.Chat.objects.create()
        chat.users.add(request.user.pk)
        chat.users.add(user_id)

    return HttpResponseRedirect(redirect_to=chat.get_absolute_url())
