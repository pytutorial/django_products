from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'        

class PurchaseForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=30)
    address = forms.CharField(max_length=300)
            