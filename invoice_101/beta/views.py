# Create your views here.
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from .models import Subscription
from .serializer import SubscriptionSerializer


class SubscriptionViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [AllowAny]
