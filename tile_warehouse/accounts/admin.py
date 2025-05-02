# # accounts/admin.py
# from django.contrib import admin
# from .models import User

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass


from django.contrib import admin

# Import the models from their respective apps
from warehouse.models import Warehouse
from floor.models import Floor
from tower.models import Tower
from tiles.models import TileShipment, TileStockLocation, TileType

# Custom admin class for Warehouse
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Adjust the fields as per your model
    search_fields = ('name', 'location',)  # Searchable fields
    list_filter = ('name','location')  # Filter by creation date (if applicable)
    ordering = ('name',)  # Order by most recent creation

# Custom admin class for Floor
class FloorAdmin(admin.ModelAdmin):
    list_display = ('number', 'warehouse')  # Adjust fields as per model
    search_fields = ('number','warehouse',)  # Searchable fields
    # search_fields = ('number', 'warehouse__name')
    list_filter = ('warehouse', 'number')  # Filters for warehouse and creation date

# Custom admin class for Tower
class TowerAdmin(admin.ModelAdmin):
    list_display = ('tower_id', 'floor')  # Adjust fields as per model
    search_fields = ('tower_id',)  # Searchable fields
    list_filter = ('tower_id', 'floor')  # Filters for floor and creation date

# Custom admin class for TileStackItem
# --- TileShipment Admin ---
class TileShipmentAdmin(admin.ModelAdmin):
    list_display = ('tile_type', 'production_date', 'arrival_date', 'total_quantity')
    search_fields = ('tile_type__name', 'tile_type__brand')
    list_filter = ('arrival_date', 'tile_type__brand')

# --- TileStockLocation Admin ---
class TileStockLocationAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'warehouse', 'floor', 'tower', 'quantity')
    search_fields = ('shipment__tile_type__name', 'warehouse__name', 'tower__tower_id')
    list_filter = ('warehouse', 'floor', 'tower')


# Register the models and their custom admin classes
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Tower, TowerAdmin)
admin.site.register(TileShipment, TileShipmentAdmin)
admin.site.register(TileStockLocation, TileStockLocationAdmin)