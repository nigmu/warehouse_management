from django.shortcuts import render
from rest_framework import viewsets
from .models import Warehouse, Block
from .serializers import WarehouseSerializer, BlockSerializer
# Create your views here.

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer