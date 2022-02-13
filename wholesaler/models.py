from django.db import models
from accounts.models import customUser
from products.models import Product_packed, Product_unpacked
# Create your models here.

class business_financial_information(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE,related_name="wholesaler_business_financial_information_related", related_query_name="wholesaler_business_financial_informations")
    PAN = models.CharField(max_length=10, primary_key=True)
    GSTIN = models.CharField(max_length=15, null=False)
    IFSC = models.CharField(max_length=45, null=False)
    account_number = models.CharField(max_length=45, null= False)
    beneficiary_name = models.CharField(max_length=45, null=False)
    KYC = models.CharField(max_length=45, null=False, default=False)
    UPI = models.CharField(max_length=45, null=True)
    verified = models.BooleanField(null=False, default=False)
    wholesaler_business_info_complete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return (str(self.user_id))

class payment_information(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE,related_name="wholesaler_payment_information_realated", related_query_name="wholesaler_payment_informations")

class credit_card(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE,related_name="wholesaler_credit_card_realated", related_query_name="wholesaler_credit_card")
    mobile = models.IntegerField(primary_key=True, null=False)
    ccard_number = models.IntegerField()
    exp_date = models.DateField()
    provider = models.CharField(max_length=45)
    wholesaler_ccard_info_complete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return (self.user_id)

class debit_card(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE,related_name="wholesaler_debit_card_related",related_query_name="wholesaler_debit_cards")
    mobile = models.IntegerField(primary_key=True, null=False)
    dcard_number = models.IntegerField()
    exp_date = models.DateField()
    provider = models.CharField(max_length=45)
    wholesaler_dcard_table_complete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return (self.user_id)

class owner_details(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE,related_name="wholesaler_owner_details_related",related_query_name="wholesaler_owner_detailss")

class wholesaler_inventory(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE ,related_name="wholesaler_wholesaler_inventory_related",related_query_name="wholesaler_wholesaler_inventorys")
    packed_products = models.ManyToManyField(Product_packed, null=True, blank=True)
    unpacked_products = models.ManyToManyField(Product_unpacked, null= True, blank=True)

    def __str__(self):
        return (str(self.user_id) + ' ' + str(self.packed_products))

class wholesaler_order_list(models.Model): #to store order wholesaler has recived
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE,related_name="wholesaler_wholesaler_order_list_related",related_query_name="wholesaler_wholesaler_order_lists")
    packed_products = models.ManyToManyField(Product_packed, null=True, blank=True)
    unpacked_products = models.ManyToManyField(Product_unpacked, null= True, blank=True)
