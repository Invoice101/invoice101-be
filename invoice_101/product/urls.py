from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
app_name = "product"

router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]