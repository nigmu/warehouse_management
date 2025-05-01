from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import TileStackItem
from .forms import TileForm

def home(request):
    return render(request, 'home.html')

# List of tiles
def tile_list(request):
    tiles = TileStackItem.objects.all()
    return render(request, 'tiles/list.html', {'tiles': tiles})

# Add new tile
def tile_add(request):
    if not request.user.has_perm('tiles.add_tilestackitem'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = TileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tiles:tile_list')
    else:
        form = TileForm()
    
    return render(request, 'tiles/form.html', {'form': form, 'title': 'Add New Tile'})

# Edit existing tile
def tile_edit(request, pk):
    tile = get_object_or_404(TileStackItem, pk=pk)
    
    if not request.user.has_perm('tiles.change_tilestackitem'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = TileForm(request.POST, request.FILES, instance=tile)
        if form.is_valid():
            form.save()
            return redirect('tiles:tile_list')
    else:
        form = TileForm(instance=tile)
    
    return render(request, 'tiles/form.html', {'form': form, 'title': 'Edit Tile'})

# Delete a tile
def tile_delete(request, pk):
    tile = get_object_or_404(TileStackItem, pk=pk)
    
    if not request.user.has_perm('tiles.delete_tilestackitem'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        tile.delete()
        return redirect('tiles:tile_list')
    
    return render(request, 'tiles/delete.html', {'object': tile})
