# Create your views here.
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from .models import BetaSubscription
from .serializer import BetaSubscriptionSerializer


class BetaSubscriptionViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = BetaSubscriptionSerializer
    queryset = BetaSubscription.objects.all()
    permission_classes = [AllowAny]
