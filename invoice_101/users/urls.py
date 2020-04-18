from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, SignUpViewSet

router = DefaultRouter()
app_name = "users"

router.register('signup', SignUpViewSet)
router.register('user', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
