from django.urls import include, path
from rest_framework.routers import DefaultRouter

from invoice_101.contact.views import ContactViewSet

router = DefaultRouter()
app_name = "contact"

router.register('contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
