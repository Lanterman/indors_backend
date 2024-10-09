from django.contrib import admin

from . import models


@admin.register(models.Cat)
class CatAdmin(admin.ModelAdmin):
    """Cat admin"""

    list_display = ("id", "name", "age", "owner_id", "created_in")
    list_display_links = ("id", "name", "age", "owner_id", "created_in")
    fields = ("name", "age", "breed", "hairiness", "owner_id")
    search_fields = ("name", )
    list_filter = ("hairiness", )
    list_max_show_all = 250
    list_per_page = 150


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    """Chat admin"""

    list_display = ("id", "created_in")
    list_display_links = ("id", "created_in")
    fields = ("users",)
    list_max_show_all = 250
    list_per_page = 150
    list_select_related = True
    raw_id_fields = ("users", )


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Message admin"""

    list_display = ("id", "chat_id", "owner_id", "created_in")
    list_display_links = ("id", "chat_id", "owner_id", "created_in")
    fields = ("message", "chat_id", "owner_id")
    list_max_show_all = 250
    list_per_page = 150
