from rest_framework.permissions import BasePermission, SAFE_METHODS


class BlogPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_admin:
            return True

        if request.user.is_author:
            return True

        if request.user.is_reader:
            return request.method in SAFE_METHODS

        return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_admin:
            return True

        if request.user.is_author:
            return obj.author == request.user

        if request.user.is_reader:
            return obj.is_published and request.method in SAFE_METHODS

        return False
