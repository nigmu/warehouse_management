from django import forms
from .models import Floor

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['warehouse', 'number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
