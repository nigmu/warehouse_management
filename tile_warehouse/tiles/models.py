from django.db import models
from tower.models import Tower  # Import Tower model
from django.conf import settings

class TileStackItem(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    tile_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    production_date = models.DateField()
    stacking_date = models.DateField()
    sales_count = models.PositiveIntegerField(default=0)
    remaining_count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='tile_images/', null=True, blank=True)

    # Relationships
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE, related_name='tile_stacks')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='tile_entries')

    # Denormalized meta fields for fast querying & searching
    warehouse_name = models.CharField(max_length=100)
    floor_number = models.PositiveIntegerField()
    tower_identifier = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Auto-fill denormalized fields
        self.warehouse_name = self.tower.floor.warehouse.name
        self.floor_number = self.tower.floor.number
        self.tower_identifier = self.tower.tower_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tile_name} | {self.serial_number} | {self.remaining_count} pcs"
