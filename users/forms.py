# forms.py

from django import forms
from .models import Menu, Employee, Quote

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['item', 'price', 'category', 'image']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'caption', 'employee_message', 'image']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'quote_by', 'image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)