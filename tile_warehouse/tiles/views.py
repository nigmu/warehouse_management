from django.shortcuts import render, redirect, get_object_or_404
from .models import TileShipment, TileStockLocation, TileType
from .forms import TileShipmentForm, TileStockLocationForm, TileTypeForm
from .utils import suggest_towers
from tower.models import Tower
from django.shortcuts import get_object_or_404

# --------------------------------------------------------------------
# ----- TileType CRUD -----
def type_list(request):
    types = TileType.objects.all()
    return render(request, 'tiles/type_list.html', {'types': types})

def type_create(request):
    if request.method == 'POST':
        form = TileTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tiles:type_list')
    else:
        form = TileTypeForm()
    return render(request, 'tiles/type_form.html', {'form': form})

def type_detail(request, pk):
    tile_type = get_object_or_404(TileType, pk=pk)
    return render(request, 'tiles/type_detail.html', {'type': tile_type})

def type_update(request, pk):
    tile_type = get_object_or_404(TileType, pk=pk)
    if request.method == 'POST':
        form = TileTypeForm(request.POST, instance=tile_type)
        if form.is_valid():
            form.save()
            return redirect('tiles:type_detail', pk=pk)
    else:
        form = TileTypeForm(instance=tile_type)
    return render(request, 'tiles/type_form.html', {'form': form})

def type_delete(request, pk):
    tile_type = get_object_or_404(TileType, pk=pk)
    if request.method == 'POST':
        tile_type.delete()
        return redirect('tiles:type_list')
    return render(request, 'tiles/type_confirm_delete.html', {'type': tile_type})



# ---------------------------------------------------------------------------------------------
# ----- TileStockLocation CRUD -----
def stock_list(request):
    stock_points = TileStockLocation.objects.select_related(
        'shipment','warehouse','floor','tower'
    )
    return render(request, 'tiles/stock_list.html', {'stock_points': stock_points})

def stock_create(request):
    if request.method == 'POST':
        form = TileStockLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tiles:stock_list')
    else:
        form = TileStockLocationForm()
    return render(request, 'tiles/stock_form.html', {'form': form})

def stock_detail(request, pk):
    loc = get_object_or_404(TileStockLocation, pk=pk)
    return render(request, 'tiles/stock_detail.html', {'loc': loc})

def stock_update(request, pk):
    loc = get_object_or_404(TileStockLocation, pk=pk)
    if request.method == 'POST':
        form = TileStockLocationForm(request.POST, instance=loc)
        if form.is_valid():
            form.save()
            return redirect('tiles:stock_detail', pk=pk)
    else:
        form = TileStockLocationForm(instance=loc)
    return render(request, 'tiles/stock_form.html', {'form': form})

def stock_delete(request, pk):
    loc = get_object_or_404(TileStockLocation, pk=pk)
    if request.method == 'POST':
        loc.delete()
        return redirect('tiles:stock_list')
    return render(request, 'tiles/stock_confirm_delete.html', {'loc': loc})


# -----------------------------------------------------------------------------------------------------------------------
# ----- TileShipment CRUD -----
def shipment_list(request):
    shipments = TileShipment.objects.all()
    return render(request, 'tiles/shipment_list.html', {'shipments': shipments})


def shipment_create(request):
    if request.method == 'POST':
        form = TileShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save()
            suggestions = suggest_towers(shipment.total_quantity)
            for tower, qty in suggestions:
                TileStockLocation.objects.create(
                    shipment=shipment,
                    tower=tower,
                    warehouse=tower.floor.warehouse,
                    floor=tower.floor,
                    quantity=qty
                )
            return redirect('tiles:shipment_list')
    else:
        form = TileShipmentForm()
    return render(request, 'tiles/shipment_form.html', {'form': form})


def shipment_update(request, pk):
    shipment = get_object_or_404(TileShipment, pk=pk)
    if request.method == 'POST':
        form = TileShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')
    else:
        form = TileShipmentForm(instance=shipment)
    return render(request, 'tiles/shipment_form.html', {'form': form})


def shipment_detail(request, pk):
    shipment = get_object_or_404(TileShipment, pk=pk)
    locations = TileStockLocation.objects.filter(shipment=shipment)
    return render(request, 'tiles/shipment_detail.html', {
        'shipment': shipment,
        'locations': locations
    })


def shipment_delete(request, pk):
    shipment = get_object_or_404(TileShipment, pk=pk)
    if request.method == 'POST':
        shipment.delete()
        return redirect('tiles:shipment_list')
    return render(request, 'tiles/shipment_confirm_delete.html', {'shipment': shipment})
