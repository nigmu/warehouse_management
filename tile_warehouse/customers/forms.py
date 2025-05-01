# forms.py
from django import forms
from .models import Customer, PhoneNumber
from django.forms import inlineformset_factory

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'remarks']

class PhoneNumberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the first form's number field required
        if self.prefix == 'phone_numbers-0':
            self.fields['number'].required = True
    
    class Meta:
        model = PhoneNumber
        fields = ['number']  # Removed 'is_primary' from fields
        widgets = {
            'number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }

PhoneNumberFormSet = inlineformset_factory(
    Customer,
    PhoneNumber,
    form=PhoneNumberForm,
    extra=2,  # Shows 3 forms total (1 required + 2 optional)
    can_delete=False,
    min_num=1,  # At least one phone number is required
    validate_min=True
)