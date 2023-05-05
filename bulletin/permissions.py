from rest_framework import permissions

class IsCaptainOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow captains and admins to perform actions on their own ships
        if request.user.is_authenticated:
            return request.user == obj.captain or request.user == obj.admin
        return False
