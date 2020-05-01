from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StateViewSet, GSTSlabViewSet, UOMViewSet

router = DefaultRouter()
app_name = "core"

router.register('state', StateViewSet)
router.register('gst_slab', GSTSlabViewSet)
router.register('uom', UOMViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
