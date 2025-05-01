from django.contrib import admin
from .models import Customer, PhoneNumber

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_primary_number', 'address')
    search_fields = ('name', 'phone_numbers__number')
    inlines = [PhoneNumberInline]

    def get_primary_number(self, obj):
        primary = obj.phone_numbers.filter(is_primary=True).first()
        return primary.number if primary else '—'
    get_primary_number.short_description = 'Primary Phone'

admin.site.register(Customer, CustomerAdmin)
