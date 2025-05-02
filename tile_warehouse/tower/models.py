from django.db import models
from floor.models import Floor  # Import Floor model
from django.utils import timezone

class Tower(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='towers')
    tower_id = models.CharField(max_length=50)
    max_capacity = models.PositiveIntegerField(default=100)

    # Denormalized fields
    warehouse = models.ForeignKey('warehouse.Warehouse', on_delete=models.CASCADE, default=1)

    @property
    def available_capacity(self):
        max_capacity = self.max_capacity  # Replace with your actual field name
        used_quantity = sum(loc.quantity for loc in self.tilestocklocation_set.all())
        return max_capacity - used_quantity


    def save(self, *args, **kwargs):
        self.warehouse = self.floor.warehouse
        super().save(*args, **kwargs)
