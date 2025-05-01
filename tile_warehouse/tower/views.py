from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Tower
from .forms import TowerForm

def home(request):
    return render(request, 'home.html')

# List of towers
def tower_list(request):
    towers = Tower.objects.all()
    return render(request, 'tower/list.html', {'towers': towers})

# Add new tower
def tower_add(request):
    if not request.user.has_perm('tower.add_tower'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = TowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tower:tower_list')
    else:
        form = TowerForm()
    
    return render(request, 'tower/form.html', {'form': form, 'title': 'Add New Tower'})

# Edit existing tower
def tower_edit(request, pk):
    tower = get_object_or_404(Tower, pk=pk)
    
    if not request.user.has_perm('tower.change_tower'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = TowerForm(request.POST, instance=tower)
        if form.is_valid():
            form.save()
            return redirect('tower:tower_list')
    else:
        form = TowerForm(instance=tower)
    
    return render(request, 'tower/form.html', {'form': form, 'title': 'Edit Tower'})

# Delete a tower
def tower_delete(request, pk):
    tower = get_object_or_404(Tower, pk=pk)
    
    if not request.user.has_perm('tower.delete_tower'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        tower.delete()
        return redirect('tower:tower_list')
    
    return render(request, 'tower/delete.html', {'object': tower})
