from rest_framework.permissions import BasePermission, SAFE_METHODS

class BlogPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

     
        if not user.is_authenticated:
            return False

  
        if getattr(user, "is_admin", False):
            return True

       
        if getattr(user, "is_author", False):
            return True

    
        if getattr(user, "is_reader", False):
            return request.method in SAFE_METHODS

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False

   
        if getattr(user, "is_admin", False):
            return True

       
        if getattr(user, "is_author", False):
            return obj.author == user

        if getattr(user, "is_reader", False):
            return obj.is_published and request.method in SAFE_METHODS

        return False
