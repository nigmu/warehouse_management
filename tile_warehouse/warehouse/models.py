from django.db import models
from django.utils import timezone


class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.TextField(blank=True)

    def __str__(self):
        return self.name
