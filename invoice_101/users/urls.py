from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
app_name = "users"

router.register('user', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
