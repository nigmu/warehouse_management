from django.shortcuts import render
from rest_framework import viewsets
from .models import Warehouse, Block
from .serializers import WarehouseSerializer, BlockSerializer
# Create your views here.

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

def warehouse_page(request):
    return render(request, 'warehouse/warehouse_page.html')



# ----------------------------------------------------------------------------------

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

def block_page(request):
    return render(request, 'block/block_page.html')



# ----------------------------------------------------------------------------------

# Index page
def index(request):
    return render(request, 'index.html')




