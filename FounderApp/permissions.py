from  rest_framework import permissions
from . import views


class Found_Permissions(permissions.BasePermission):
    """Allow the user to edit its own post"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
