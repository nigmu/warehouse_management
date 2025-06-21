from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StackViewSet, search_stock_by_tile

router = DefaultRouter()
router.register(r'stacks', StackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search_stock_by_tile),
]