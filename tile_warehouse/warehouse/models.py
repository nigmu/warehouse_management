from django.contrib.auth.models import AbstractUser
from django.db import models


# ────────────────────────────────────────────────
# USERS MODEL
# ────────────────────────────────────────────────
class User(AbstractUser):
    ROLE_CHOICES = [
        ('developer', 'Developer'),
        ('owner', 'Owner'),
        ('worker', 'Worker'),
        ('viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_users')

    def __str__(self):
        return f"{self.username} ({self.role})"



from django.db import models
from django.conf import settings

# ────────────────────────────────────────────────
# 📦 WAREHOUSE MODEL
# ────────────────────────────────────────────────
class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ────────────────────────────────────────────────
# 🧱 FLOOR MODEL (Linked to Warehouse)
# ────────────────────────────────────────────────
class Floor(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='floors')
    number = models.PositiveIntegerField()

    class Meta:
        unique_together = ('warehouse', 'number')

    def __str__(self):
        return f"{self.warehouse.name} - Floor {self.number}"


# ────────────────────────────────────────────────
# 🏢 TOWER MODEL (Linked to Floor)
# ────────────────────────────────────────────────
class Tower(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='towers')
    tower_id = models.CharField(max_length=50)

    class Meta:
        unique_together = ('floor', 'tower_id')

    def __str__(self):
        return f"{self.floor} - Tower {self.tower_id}"


# ────────────────────────────────────────────────
# 🧩 TILE STACK ITEM MODEL
# ────────────────────────────────────────────────
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
