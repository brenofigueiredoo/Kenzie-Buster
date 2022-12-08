from rest_framework import permissions


class IsOwnerOrEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_employee:
            return True

        if obj == request.user:
            return True
