from django.db import models

class Tile(models.Model): 
    tile_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('tile_name', 'brand', 'size') # Ensures that the combination of tile_name, brand, and size is unique

    def __str__(self):
        return f"{self.tile_name} ({self.brand}, {self.size})"

