from django.core.validators import RegexValidator
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


GSTValidator = RegexValidator(r'^\d{2}[a-zA-Z]{5}\d{4}[a-zA-Z][a-zA-Z\d][zZ][a-zA-Z\d]$', 'Invalid GST.')
PinCodeValidator = RegexValidator(r'^\d{6}$', 'Invalid PinCode.')
