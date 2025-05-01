from django import forms
from .models import Warehouse

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['created_at'].widget = forms.DateInput(attrs={'type': 'date'})
