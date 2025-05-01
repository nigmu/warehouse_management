from django.db import models
from floor.models import Floor  # Import Floor model
from django.utils import timezone

class Tower(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='towers')
    tower_id = models.CharField(max_length=50)
    created_at = models.DateField(null=True, blank=True)  # Allow the field to be manually set

    class Meta:
        unique_together = ('floor', 'tower_id')


    def __str__(self):
        return f"{self.floor} - Tower {self.tower_id}"
    
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()  # You can set a default time if none is provided
        super().save(*args, **kwargs)
