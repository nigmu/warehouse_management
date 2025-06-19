from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, BlockViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'blocks', BlockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]