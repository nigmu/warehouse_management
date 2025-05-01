# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm, PhoneNumberFormSet
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all().prefetch_related('phone_numbers')
    return render(request, 'customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        phone_formset = PhoneNumberFormSet(request.POST)
        if customer_form.is_valid() and phone_formset.is_valid():
            customer = customer_form.save()
            phone_numbers = phone_formset.save(commit=False)
            # Save phone numbers - first one is automatically primary
            for i, phone in enumerate(phone_numbers):
                if phone.number:  # Only save if number is provided
                    phone.customer = customer
                    phone.is_primary = (i == 0)  # First number is primary
                    phone.save()
            return redirect('customers:customer_list')
    else:
        customer_form = CustomerForm()
        phone_formset = PhoneNumberFormSet()
    return render(request, 'add_customer.html', {
        'customer_form': customer_form,
        'phone_formset': phone_formset
    })

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        phone_formset = PhoneNumberFormSet(request.POST, instance=customer)
        if customer_form.is_valid() and phone_formset.is_valid():
            customer = customer_form.save()
            # Get existing phone numbers to maintain primary status
            existing_primary = customer.phone_numbers.filter(is_primary=True).first()
            
            phone_numbers = phone_formset.save(commit=False)
            for phone in phone_numbers:
                if phone.number:  # Only save if number is provided
                    phone.customer = customer
                    # Maintain existing primary or set first as primary if none exists
                    if existing_primary and phone.id == existing_primary.id:
                        phone.is_primary = True
                    elif not existing_primary and phone == phone_numbers[0]:
                        phone.is_primary = True
                    else:
                        phone.is_primary = False
                    phone.save()
            return redirect('customers:customer_list')
    else:
        customer_form = CustomerForm(instance=customer)
        phone_formset = PhoneNumberFormSet(instance=customer)
    return render(request, 'edit_customer.html', {
        'customer_form': customer_form,
        'phone_formset': phone_formset
    })

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customer_list')
    return render(request, 'delete_customer.html', {'customer': customer})