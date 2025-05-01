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
from tiles.models import TileStackItem  # Assuming TileStackItem is in the tiles app

# Custom admin class for Warehouse
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at')  # Adjust the fields as per your model
    search_fields = ('name', 'location')  # Searchable fields
    list_filter = ('created_at',)  # Filter by creation date (if applicable)
    ordering = ('created_at',)  # Order by most recent creation

# Custom admin class for Floor
class FloorAdmin(admin.ModelAdmin):
    list_display = ('number', 'warehouse', 'created_at')  # Adjust fields as per model
    search_fields = ('number',)  # Searchable fields
    list_filter = ('warehouse', 'created_at')  # Filters for warehouse and creation date

# Custom admin class for Tower
class TowerAdmin(admin.ModelAdmin):
    list_display = ('tower_id', 'floor', 'created_at')  # Adjust fields as per model
    search_fields = ('tower_id',)  # Searchable fields
    list_filter = ('tower_id', 'floor', 'created_at')  # Filters for floor and creation date

# Custom admin class for TileStackItem
class TileStackItemAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'tile_name', 'brand', 'production_date', 'stacking_date', 'sales_count', 'remaining_count', 'warehouse_name', 'floor_number', 'tower_identifier')  # Adjust based on your model
    search_fields = ('tile_name', 'warehouse_name', 'floor_number', 'tower_identifier', 'brand', 'production_date', 'stacking_date')  # Assuming related fields
    list_filter = ('serial_number', 'tile_name', 'brand', 'production_date', 'stacking_date', 'sales_count', 'remaining_count', 'warehouse_name', 'floor_number', 'tower_identifier')  # Filters by warehouse and floor

# Register the models and their custom admin classes
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Tower, TowerAdmin)
admin.site.register(TileStackItem, TileStackItemAdmin)
