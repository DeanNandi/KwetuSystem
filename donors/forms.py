from django import forms
from .models import Donors
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MyForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = ['product_name', 'supplier', 'quantity', 'recipient', 'employee_id', 'date_of_payment']
        labels = {'product_name': 'Product Name', 'supplier': 'Who Supplied', 'quantity': 'Quantity',
                  'recipient': 'Received By', 'employee_id': 'Employee ID', 'date_of_payment': 'Date In'}
