from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow only the owner of object to edit it"""

    def has_object_permission(self, request, view, obj):

        """Check if permission is allowed to any request"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
