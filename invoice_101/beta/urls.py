from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BetaSubscriptionViewSet

router = DefaultRouter()
app_name = "beta"

router.register('subscription', BetaSubscriptionViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
