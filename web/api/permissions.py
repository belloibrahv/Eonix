from rest_framework.permissions import BasePermission, SAFE_METHODS 

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission class. Allows read-only access for any request,
    but write access (POST, PUT, DELETE) is restricted to admin users.
    """
    def has_permission(self, request, view):
        # SAFE_METHODS are HTTP methods like GET, HEAD, and OPTIONS
        if request.method in SAFE_METHODS:
            return True
        # Only allow modification if the user is an admin
        return request.user and request.user.is_staff
