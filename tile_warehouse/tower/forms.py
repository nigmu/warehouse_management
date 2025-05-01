from django import forms
from .models import Tower

class TowerForm(forms.ModelForm):
    class Meta:
        model = Tower
        fields = ['floor', 'tower_id', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].widget = forms.DateInput(attrs={'type': 'date'})
