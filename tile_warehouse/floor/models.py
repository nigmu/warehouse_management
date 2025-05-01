from django.db import models
from warehouse.models import Warehouse  # Import Warehouse model
from django.utils import timezone

class Floor(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='floors')
    number = models.PositiveIntegerField()
    created_at = models.DateField(null=True, blank=True)  # Allow the field to be manually set

    class Meta:
        unique_together = ('warehouse', 'number')

    def __str__(self):
        return f"{self.warehouse.name} - Floor {self.number}"
    
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()  # You can set a default time if none is provided
        super().save(*args, **kwargs)
