from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Floor
from .forms import FloorForm

def home(request):
    return render(request, 'home.html')

# List of floors
def floor_list(request):
    floors = Floor.objects.all()
    return render(request, 'floor/list.html', {'floors': floors})

# Add new floor
def floor_add(request):
    if not request.user.has_perm('floor.add_floor'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = FloorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('floor:floor_list')
    else:
        form = FloorForm()
    
    return render(request, 'floor/form.html', {'form': form, 'title': 'Add New Floor'})

# Edit existing floor
def floor_edit(request, pk):
    floor = get_object_or_404(Floor, pk=pk)
    
    if not request.user.has_perm('floor.change_floor'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = FloorForm(request.POST, instance=floor)
        if form.is_valid():
            form.save()
            return redirect('floor:floor_list')
    else:
        form = FloorForm(instance=floor)
    
    return render(request, 'floor/form.html', {'form': form, 'title': 'Edit Floor'})

# Delete a floor
def floor_delete(request, pk):
    floor = get_object_or_404(Floor, pk=pk)
    
    if not request.user.has_perm('floor.delete_floor'):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        floor.delete()
        return redirect('floor:floor_list')
    
    return render(request, 'floor/delete.html', {'object': floor})
