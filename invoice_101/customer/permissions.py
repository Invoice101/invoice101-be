from rest_framework.permissions import IsAuthenticated


class CustomerPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
