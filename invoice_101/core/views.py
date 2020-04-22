from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from .models import State
from .serializers import StateSerializer


class StateViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [AllowAny]
