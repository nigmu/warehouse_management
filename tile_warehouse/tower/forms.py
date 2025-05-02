from django import forms
from .models import Tower

class TowerForm(forms.ModelForm):
    class Meta:
        model = Tower
        fields = ['floor', 'tower_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
