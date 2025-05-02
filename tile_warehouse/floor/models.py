from django.db import models
from warehouse.models import Warehouse  # Import Warehouse model
from django.utils import timezone

class Floor(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='floors')
    number = models.PositiveIntegerField()

    class Meta:
        unique_together = ('warehouse', 'number')

    def __str__(self):
        return f"{self.warehouse.name} - Floor {self.number}"

