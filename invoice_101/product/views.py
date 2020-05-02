# Create your views here.
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Product
from .permissions import ProductPermission
from .serializers import ProductSerializer
from ..utils.common_utils import StandardResultsSetPagination


class ProductViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'hsn_sac',)
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
