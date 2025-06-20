from django.shortcuts import render
from rest_framework import viewsets
from .models import Tile
from .serializers import TileSerializer

class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer

def tile_page(request):
    return render(request, 'tile/tile_page.html')