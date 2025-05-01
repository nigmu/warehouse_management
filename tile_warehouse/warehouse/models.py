from django.db import models
from django.utils import timezone


class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.TextField(blank=True)
    # created_at = models.DateField(null=True, blank=True)  # Allow the field to be manually set

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     if not self.created_at:
    #         self.created_at = timezone.now()  # You can set a default time if none is provided
    #     super().save(*args, **kwargs)
