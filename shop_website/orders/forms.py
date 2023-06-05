from django import forms
from .models import Order


# Это форма, которая будет использоваться для создания
# новых объектов Order.
class OrderCreateForm(forms.ModelForm):
    # название поля над инпутом в форме ордера
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'order-form'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'order-form'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'order-form'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'order-form'}))
    postal_code = forms.CharField(label='Postal code', widget=forms.TextInput(attrs={'class': 'order-form'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'order-form'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']