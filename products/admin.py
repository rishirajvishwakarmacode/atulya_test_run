from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product_packed)
class Product_packedadmin(admin.ModelAdmin):
    list_filter = ['name', 'id', 'mrp', 'hsn_code']

@admin.register(Product_unpacked)
class Product_unpackedadmin(admin.ModelAdmin):
    list_filter = ['name', 'id', 'hsn_code']

@admin.register(Brand)
class Brandsadmin(admin.ModelAdmin):
    list_filter = ['name', 'description']