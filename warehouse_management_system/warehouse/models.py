from django.db import models

# Defines the Warehouse database
class Warehouse(models.Model): 
    warehouse_name = models.CharField(unique=True, null=False, blank=False, max_length=100) #each warehouse has a unique name and cannot be null or blank
    warehouse_location = models.CharField(max_length=255)

    def __str__(self):
        return self.warehouse_name

# Defines the Block database
class Block(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='blocks')
    block_name = models.CharField(null=False, blank=False, max_length=20)

    class Meta:
        unique_together = ('warehouse', 'block_name')

    def __str__(self):
        return f"{self.warehouse.warehouse_name} - Block {self.block_name}"
