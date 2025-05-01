from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='phone_numbers')
    number = models.CharField(max_length=15)
    is_primary = models.BooleanField(default=False)

    class Meta:
        unique_together = ('customer', 'number')

    def save(self, *args, **kwargs):
        if self.is_primary:
            PhoneNumber.objects.filter(customer=self.customer, is_primary=True).update(is_primary=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number} ({'Primary' if self.is_primary else 'Secondary'})"
