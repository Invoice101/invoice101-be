from django.urls import include, path
from rest_framework.routers import DefaultRouter

from invoice_101.customer.views import CustomerViewSet

router = DefaultRouter()
app_name = "customer"

router.register('customer', CustomerViewSet)

url_patterns = [
    path('', include(router.urls)),
]
