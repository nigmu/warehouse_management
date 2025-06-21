from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Stack
from .serializers import StackSerializer, StockSearchSerializer
from warehouse.models import Warehouse, Block
from tile.models import Tile

class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

def stack_page(request):
    return render(request, 'stock/stock_page.html')


# This view allows searching for stock by tile name and tile size
@api_view(['GET'])
def search_stock_by_tile(request):
    tile_name = request.GET.get('tile_name')
    size = request.GET.get('size')

    if not tile_name or not size:
        return Response({'error': 'tile_name and size are required.'}, status=400)

    stacks = Stack.objects.filter(
        tile__tile_name__iexact=tile_name,
        tile__size__iexact=size
    )

    serializer = StockSearchSerializer(stacks, many=True)
    return Response(serializer.data)
