from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.business_financial_information)
admin.site.register(models.credit_card)
admin.site.register(models.debit_card)
admin.site.register(models.payment_information)
admin.site.register(models.owner_details)

@admin.register(models.retailer_inventory)
class retailerinventoryAdmin(admin.ModelAdmin):
    list_display = ['user_id']