from django import forms
from .models import TileType, TileShipment, TileStockLocation

# Form for creating/editing TileType
class TileTypeForm(forms.ModelForm):
    class Meta:
        model = TileType
        fields = ['brand', 'name']  # Fields to be displayed in the form
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tile Name'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Tile Brand'}),
        }

# Form for creating/editing TileShipment
class TileShipmentForm(forms.ModelForm):
    class Meta:
        model = TileShipment
        fields = ['tile_type', 'production_date', 'arrival_date', 'total_quantity']
        widgets = {
            'production_date': forms.DateInput(attrs={'type': 'date'}),
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'total_quantity': forms.NumberInput(attrs={'min': '1'}),
        }

# Form for creating/editing TileStockLocation
class TileStockLocationForm(forms.ModelForm):
    class Meta:
        model = TileStockLocation
        fields = ['shipment', 'warehouse', 'floor', 'tower', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': '1', 'placeholder': 'Quantity'}),
        }

    # Custom validation for quantity field to ensure it is a positive number
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be a positive number.")
        return quantity
