from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.business_financial_information)
admin.site.register(models.credit_card)
admin.site.register(models.debit_card)
admin.site.register(models.payment_information)
admin.site.register(models.owner_details)
admin.site.register(models.retailer_order_list)

@admin.register(models.retailer_inventory)
class retailerinventoryAdmin(admin.ModelAdmin):
    list_display = ['user_id']

