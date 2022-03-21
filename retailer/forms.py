from django import forms
from accounts.models import customUser

class retailer_details_form(forms.Form):
    retail_store_pan = forms.CharField(max_length=100)
    retail_store_gst = forms.CharField(max_length=100)
    retail_store_ifsc = forms.CharField(max_length=100)
    retail_store_bank_account = forms.CharField(max_length=100)
    retail_store_bank_account = forms.CharField(max_length=100)
    retail_store_name = forms.CharField(max_length=100)
    retail_store_upi = forms.CharField(max_length=100)


class addproductForm(forms.Form):
    pdtid = forms.UUIDField(label='Product ID')
    sellprice = forms.DecimalField(max_digits=6, decimal_places=2, label='Your Selling Price')
