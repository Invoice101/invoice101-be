from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from .models import State, GSTSlab, UOM
from .serializers import StateSerializer, GSTSlabSerializer, UOMSerializer


class StateViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [AllowAny]


class GSTSlabViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = GSTSlab.objects.all()
    serializer_class = GSTSlabSerializer


class UOMViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer
