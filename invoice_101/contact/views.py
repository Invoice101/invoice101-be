# Create your views here.
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Contact
from .permissions import ContactPermission
from .serializers import ContactSerializer
from ..utils.common_utils import StandardResultsSetPagination


class ContactViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin):
    serializer_class = ContactSerializer
    permission_classes = [ContactPermission]
    queryset = Contact.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email', 'mobile_no', 'company')

    def get_queryset(self):
        sort = self.request.query_params.get('sort', 'name')
        queryset = self.queryset.order_by(sort)

        queryset = queryset.filter(user=self.request.user)
        return queryset