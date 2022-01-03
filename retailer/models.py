from django.db import models
from accounts.models import customUser
# Create your models here.
class business_financial_information(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
    PAN = models.CharField(max_length=10, primary_key=True)
    GSTIN = models.CharField(max_length=15, null=False)
    IFSC = models.CharField(max_length=45, null=False)
    account_number = models.CharField(max_length=45, null= False)
    beneficiary_name = models.CharField(max_length=45, null=False)
    KYC = models.CharField(max_length=45, null=False)
    UPI = models.CharField(max_length=45, null=True)
    verified = models.BooleanField(null=False)

class payment_information(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)

class credit_card(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
    mobile = models.IntegerField(primary_key=True, null=False)
    ccard_number = models.IntegerField()
    exp_date = models.DateField()
    provider = models.CharField(max_length=45)

class debit_card(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
    mobile = models.IntegerField(primary_key=True, null=False)
    dcard_number = models.IntegerField()
    exp_date = models.DateField()
    provider = models.CharField(max_length=45)


class owner_details(models.Model):
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
