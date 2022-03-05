from django.db import models
from accounts.models import customUser
from products.models import Product_packed, Product_unpacked, Brand

class wslbi(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    pan = models.CharField(max_length=10)
    gstin = models.CharField(max_length=15, null=False)
    ifsc = models.CharField(max_length=45, null=False)
    account_number = models.CharField(max_length=45, null= False)
    beneficiary_name = models.CharField(max_length=45, null=False)
    kyc = models.CharField(max_length=45, null=False, default=False)
    upi = models.CharField(max_length=45, null=True)
    verified = models.BooleanField(null=False, default=False)
    retailer_business_info_complete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return (str(self.user_id))

class wslbrd(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    brands = models.ManyToManyField(Brand)

    def __str__(self):
        return(str(self.user_id) + " brands")

class wslinvt(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    packed_products = models.ManyToManyField(Product_packed, null=True, through='wslproddtl')
    unpacked_products = models.ManyToManyField(Product_unpacked, null= True)

    def __str__(self):
        return (str(self.user_id) + " inventory")

class wslproddtl(models.Model):
    wholesaler = models.ForeignKey(wslinvt, on_delete=models.CASCADE)
    product = models.ForeignKey(Product_packed, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    sellprice = models.CharField(max_length=5, null=True)