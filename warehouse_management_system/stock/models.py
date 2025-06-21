from django.db import models
from warehouse.models import Warehouse, Block
from tile.models import Tile

class Stack(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    manufacturing_date = models.DateField(null=True, blank=True)
    shipment_arrival_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Stack {self.tile.tile_name} is in Block {self.block.block_name} of Warehouse {self.warehouse.warehouse_name} with {self.quantity} boxes"