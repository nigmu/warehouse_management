from django import forms
from .models import TileStackItem

class TileForm(forms.ModelForm):
    class Meta:
        model = TileStackItem
        fields = [
            'serial_number','tile_name','brand','production_date',
            'stacking_date','sales_count','remaining_count','image','tower'
        ]


    # Customizing the date fields to show a date picker (calendar dropdown)
    production_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    
    stacking_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
