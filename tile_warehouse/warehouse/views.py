from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Warehouse
from .forms import WarehouseForm

def home(request):
    return render(request, 'home.html')

# List of warehouses
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse/list.html', {'warehouses': warehouses})

# Add new warehouse
def warehouse_add(request):
    if not request.user.has_perm('warehouse.add_warehouse'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse:warehouse_list')
    else:
        form = WarehouseForm()
    
    return render(request, 'warehouse/form.html', {'form': form, 'title': 'Add New Warehouse'})

# Edit existing warehouse
def warehouse_edit(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    
    if not request.user.has_perm('warehouse.change_warehouse'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('warehouse:warehouse_list')
    else:
        form = WarehouseForm(instance=warehouse)
    
    return render(request, 'warehouse/form.html', {'form': form, 'title': 'Edit Warehouse'})

# Delete a warehouse
def warehouse_delete(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    
    if not request.user.has_perm('warehouse.delete_warehouse'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        warehouse.delete()
        return redirect('warehouse:warehouse_list')
    
    return render(request, 'warehouse/delete.html', {'object': warehouse})
