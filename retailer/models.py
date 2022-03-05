from django.db import models
from accounts.models import customUser
from products.models import Product_packed, Product_unpacked
# Create your models here.
class retbi(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
    pan = models.CharField(max_length=10, primary_key=True)
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


class retinvt(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
    packed_products = models.ManyToManyField(Product_packed, null=True, blank=True, through='retproddtl')
    unpacked_products = models.ManyToManyField(Product_unpacked, null= True, blank=True)

    def __str__(self):
        return (str(self.user_id) + ' ' + str(self.packed_products))

class retproddtl(models.Model):
    retailer = models.ForeignKey(retinvt, on_delete=models.CASCADE)
    packed_product = models.ForeignKey(Product_packed, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    sellprice = models.CharField(max_length=5, null=True)

    def __str__(self):
        return (str(self.retailer) + "|" + str(self.packed_product))










