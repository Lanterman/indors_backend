from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """If owner - everything is allowed, otherwise access is denied"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user.id == obj.owner_id.id)


class IsExistsInChat(BasePermission):
    """Allow access if user is in chat"""

    def has_object_permission(self, request, view, obj):
        print(request.user.id, obj.users.all())
        return request.user in obj.users.all()