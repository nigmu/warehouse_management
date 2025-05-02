from django.db import models
from warehouse.models import Warehouse
from floor.models import Floor
from tower.models import Tower

from django.conf import settings

class TileType(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)

    class Meta:
        unique_together = ('name', 'brand')

    def __str__(self):
        return f"{self.brand} - {self.name}"


class TileShipment(models.Model):
    tile_type = models.ForeignKey(TileType, on_delete=models.CASCADE)
    production_date = models.DateField()
    arrival_date = models.DateField()
    total_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tile_type} | {self.arrival_date} | {self.total_quantity} pcs"


class TileStockLocation(models.Model):
    shipment = models.ForeignKey(TileShipment, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.shipment.tile_type} | {self.quantity} pcs @ {self.warehouse.name} > F{self.floor.number} > T{self.tower.tower_id}"
