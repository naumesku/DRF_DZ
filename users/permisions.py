from rest_framework.permissions import BasePermission

class IsModer(BasePermission):
    """permission для определения является ли пользователь модератором"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user == obj.owner:
#             return request.method in ('GET', 'PUT', 'PATCH', 'DELETE',)
#         return False

class IsOwner(BasePermission):
    """permission для определения является ли пользователь владельцем"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
