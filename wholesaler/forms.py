from django import forms
from accounts.models import customUser

class wholesaler_details_form(forms.Form):
    wholesale_store_pan = forms.CharField(max_length=100)
    wholesale_store_gst = forms.CharField(max_length=100)
    wholesale_store_ifsc = forms.CharField(max_length=100)
    wholesale_store_bank_account = forms.CharField(max_length=100)
    wholesale_store_bank_account = forms.CharField(max_length=100)
    wholesale_store_name = forms.CharField(max_length=100)
    wholesale_store_upi = forms.CharField(max_length=100)