from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class Userpermission(permissions.BasePermission):

    message = '你没有权限~'

    def has_permission(self, request, view):
        if request.user.user_type != 3:
            return False

        return True
