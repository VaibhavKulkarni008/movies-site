from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )


class IsAdminOrAuthenticated(BasePermission):
    def has_permission(self, request, view):

        authenticated = (request.user and request.user.is_authenticated)

        return bool(
            (request.method in SAFE_METHODS and authenticated)
            or
            (authenticated and request.user.is_staff)
        )
