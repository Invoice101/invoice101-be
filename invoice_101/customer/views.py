# Create your views here.
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Customer
from .permissions import CustomerPermission
from .serializers import CustomerSerializer
from ..utils.common_utils import StandardResultsSetPagination


class CustomerViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin):
    serializer_class = CustomerSerializer
    permission_classes = [CustomerPermission]
    queryset = Customer.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email', 'mobile_no', 'company')

    def get_queryset(self):
        sort = self.request.query_params.get('sort', 'name')
        queryset = self.get_queryset().order_by(sort)

        queryset = queryset.filter(owner=self.request.user)
        return queryset
