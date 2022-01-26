# from django.db import models
# from accounts.models import customUser
#
# class business_financial_information(models.Model):
#     wuser_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
#     PAN = models.CharField(max_length=45, primary_key=True)
#     GSTIN = models.CharField(max_length=15, null=False)
#     IFSC = models.CharField(max_length=45, null=False)
#     account_number = models.CharField(max_length=45, null= False)
#     beneficiary_name = models.CharField(max_length=45, null=False)
#     KYC = models.CharField(max_length=45, null=False)
#     UPI = models.CharField(max_length=45, null=True)
#     verified = models.BooleanField(null=False)
#     wholesaler_business_information_complete : models.BooleanField(default=False)
#
#     def __str__(self):
#         return (str(self.user_id))
