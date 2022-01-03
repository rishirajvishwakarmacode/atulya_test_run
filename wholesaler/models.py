from django.db import models
from accounts.models import customUser

# Create your models here.
# class business_financial_information(models.Model):
#     user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
#     PAN = models.CharField(max_length=45, primary_key=true)
#     GSTIN = models.CharField(max_length=15, null=False)
#     IFSC = models.CharField(max_length=45, null=False)
#     account_number = models.CharField(max_length=45, null= False)
#     beneficiary_name = models.CharField(max_length=45, null=False)
#     KYC = models.CharField(max_length=45, null=False)
#     UPI = models.CharField(max_length=45, null=True)
#     verified = models.BooleanField(null=False)
#
#     def __str__(self):
#         return PAN
# class business_information(models.Model):
#     user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return user_id
