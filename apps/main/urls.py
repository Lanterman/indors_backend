from django.urls import path

from . import views

urlpatterns = [
    path("cats/", views.ListCatView.as_view(), name="cat-list"),
    path("cats/<int:id>/", views.CatView.as_view(), name="cat-detail"),
    path("chats/", views.ListChatView.as_view(), name="chat-list"),
    path("chats/<int:id>/", views.ChatView.as_view(), name="chat-detail"),
    path("chats/<int:user_id>/create_chat/", views.create_chat_view, name="create_chat")
]