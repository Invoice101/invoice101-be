from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SubscriptionViewSet

router = DefaultRouter()
app_name = "beta"

router.register('subscription', SubscriptionViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
