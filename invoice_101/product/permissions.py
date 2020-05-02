from rest_framework.permissions import IsAuthenticated


class ProductPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.request.user == obj.user
