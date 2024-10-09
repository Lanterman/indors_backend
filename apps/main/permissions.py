from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """If owner - everything is allowed, otherwise access is denied"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user.id == obj.owner_id.id)
